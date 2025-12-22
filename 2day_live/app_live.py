from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

datas = [{"items": [{"name": "item1", "price": 10}]}]

@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    # return jsonify({'result':'success', 'data': {"feed1":"data", "feed2":"data2"}})
	return {'result':'success', 'data': {"feed1":"data", "feed2":"data2"}}

@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    return jsonify({'result':'success', 'data': {"feed1":"data"}})

@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return jsonify({'result':'success'})

@app.get("/api/v1/datas")
def get_datas():
    return {'datas':datas}

@app.post("/api/v1/datas")
def create_data():
    request_data = request.get_json()
    new_data = {"items": []}
    datas.append(new_data)
    return new_data, 201

# restful

items = []  # 간단한 데이터베이스 역할을 하는 리스트

class Item(Resource):
    # 특정 아이템 조회
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'message': 'Item not found'}, 404

    # 새 아이템 추가
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {'message': f"An item with name '{name}' already exists."}, 400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
		
	# 아이템 업데이트
    def put(self, name):
        data = request.get_json()
        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item

        # 아이템이 존재하지 않으면 새로운 아이템을 추가
        new_item = {'name': name, 'price': data['price']}
        items.append(new_item)
        return new_item
		
	# 아이템 삭제
    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': 'Item deleted'}

api.add_resource(Item, '/item/<string:name>')  # 경로 추가

if __name__ == "__main__":
    app.run(debug=True)
