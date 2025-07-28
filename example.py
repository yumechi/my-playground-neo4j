"""
Neo4j基本操作のサンプルコード
簡易的な社員データベースを作成し、データの投入と検索を行う
"""

from neo4j import GraphDatabase
import logging

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Neo4jExample:
    def __init__(self, uri, user, password):
        """Neo4jドライバーの初期化"""
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        """接続を閉じる"""
        self.driver.close()
    
    def clear_database(self):
        """データベースをクリア（テスト用）"""
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            logger.info("データベースをクリアしました")
    
    def create_employees(self):
        """社員ノードを作成"""
        employees = [
            {"name": "田中太郎", "age": 30, "department": "開発", "position": "エンジニア"},
            {"name": "佐藤花子", "age": 28, "department": "開発", "position": "シニアエンジニア"},
            {"name": "鈴木一郎", "age": 35, "department": "営業", "position": "マネージャー"},
            {"name": "高橋美咲", "age": 26, "department": "デザイン", "position": "デザイナー"},
            {"name": "山田健太", "age": 32, "department": "開発", "position": "テックリード"},
        ]
        
        with self.driver.session() as session:
            for emp in employees:
                session.run(
                    "CREATE (e:Employee {name: $name, age: $age, department: $department, position: $position})",
                    **emp
                )
            logger.info(f"{len(employees)}名の社員データを作成しました")
    
    def create_departments(self):
        """部署ノードを作成"""
        departments = [
            {"name": "開発", "budget": 5000000},
            {"name": "営業", "budget": 3000000},
            {"name": "デザイン", "budget": 2000000},
        ]
        
        with self.driver.session() as session:
            for dept in departments:
                session.run(
                    "CREATE (d:Department {name: $name, budget: $budget})",
                    **dept
                )
            logger.info(f"{len(departments)}つの部署データを作成しました")
    
    def create_relationships(self):
        """社員と部署の関係を作成"""
        with self.driver.session() as session:
            session.run("""
                MATCH (e:Employee), (d:Department)
                WHERE e.department = d.name
                CREATE (e)-[:BELONGS_TO]->(d)
            """)
            logger.info("社員と部署の関係を作成しました")
    
    def find_employees_by_department(self, department_name):
        """指定された部署の社員を検索"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (e:Employee)-[:BELONGS_TO]->(d:Department)
                WHERE d.name = $department_name
                RETURN e.name as name, e.age as age, e.position as position
                ORDER BY e.name
            """, department_name=department_name)
            
            employees = []
            for record in result:
                employees.append({
                    "name": record["name"],
                    "age": record["age"],
                    "position": record["position"]
                })
            
            return employees
    
    def find_employees_by_age_range(self, min_age, max_age):
        """年齢範囲で社員を検索"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (e:Employee)
                WHERE e.age >= $min_age AND e.age <= $max_age
                RETURN e.name as name, e.age as age, e.department as department, e.position as position
                ORDER BY e.age
            """, min_age=min_age, max_age=max_age)
            
            employees = []
            for record in result:
                employees.append({
                    "name": record["name"],
                    "age": record["age"],
                    "department": record["department"],
                    "position": record["position"]
                })
            
            return employees
    
    def find_senior_positions(self):
        """シニアポジションの社員を検索"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (e:Employee)
                WHERE e.position CONTAINS 'シニア' OR e.position CONTAINS 'マネージャー' OR e.position CONTAINS 'リード'
                RETURN e.name as name, e.position as position, e.department as department
                ORDER BY e.name
            """)
            
            employees = []
            for record in result:
                employees.append({
                    "name": record["name"],
                    "position": record["position"],
                    "department": record["department"]
                })
            
            return employees
    
    def get_department_statistics(self):
        """部署別の統計情報を取得"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (e:Employee)-[:BELONGS_TO]->(d:Department)
                RETURN d.name as department, 
                       count(e) as employee_count,
                       avg(e.age) as average_age,
                       d.budget as budget
                ORDER BY d.name
            """)
            
            stats = []
            for record in result:
                stats.append({
                    "department": record["department"],
                    "employee_count": record["employee_count"],
                    "average_age": round(record["average_age"], 1),
                    "budget": record["budget"]
                })
            
            return stats

def main():
    """メイン実行関数"""
    # Neo4j接続設定
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"
    
    # Neo4jインスタンス作成
    neo4j_example = Neo4jExample(uri, user, password)
    
    try:
        # データベースのクリア
        neo4j_example.clear_database()
        
        # データの作成
        neo4j_example.create_employees()
        neo4j_example.create_departments()
        neo4j_example.create_relationships()
        
        print("\n" + "="*50)
        print("Neo4j データ操作サンプル")
        print("="*50)
        
        # 1. 開発部の社員を検索
        print("\n【開発部の社員一覧】")
        dev_employees = neo4j_example.find_employees_by_department("開発")
        for emp in dev_employees:
            print(f"  - {emp['name']} ({emp['age']}歳, {emp['position']})")
        
        # 2. 年齢範囲での検索
        print("\n【30歳以上の社員一覧】")
        senior_employees = neo4j_example.find_employees_by_age_range(30, 40)
        for emp in senior_employees:
            print(f"  - {emp['name']} ({emp['age']}歳, {emp['department']}, {emp['position']})")
        
        # 3. シニアポジションの検索
        print("\n【シニアポジションの社員一覧】")
        senior_positions = neo4j_example.find_senior_positions()
        for emp in senior_positions:
            print(f"  - {emp['name']} ({emp['position']}, {emp['department']})")
        
        # 4. 部署別統計
        print("\n【部署別統計情報】")
        stats = neo4j_example.get_department_statistics()
        for stat in stats:
            print(f"  - {stat['department']}: {stat['employee_count']}名, "
                  f"平均年齢{stat['average_age']}歳, 予算{stat['budget']:,}円")
        
        print("\n" + "="*50)
        print("実行完了")
        print("="*50)
        
    except Exception as e:
        logger.error(f"エラーが発生しました: {e}")
    finally:
        neo4j_example.close()

if __name__ == "__main__":
    main()