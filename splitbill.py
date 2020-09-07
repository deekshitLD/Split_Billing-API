from flask import Flask, request, jsonify

app=Flask(__name__)

friends_list=[{
                    "id":0,
                    "friend_name":"Alston",
                    "phone_number":11111111,
                    "amount":0
                },
                 {
                    "id":1,
                    "friend_name":"Anisha",
                    "phone_number":22222222,
                     "amount":0
                },
                   {
                    "id":2,
                    "friend_name":"Rhea",
                    "phone_number":33333333,
                     "amount":0
                },
                   {
                      "id":3,
                       "friend_name":"Sathvik",
                       "phone_number":44444444,
                        "amount":0
                 },
                   {
                    "id":4,
                    "friend_name":"Disha",
                    "phone_number":555555555,
                     "amount":0
                    }]


@app.route('/splitbill',methods=['GET', 'POST'])
def splitbill():
    if request.method == 'GET':
        if len(friends_list) > 0:
            return jsonify(friends_list)
        else:
            'Nothing Found',404
    if request.method == 'POST':
        new_amount = request.form['amount']
        new_name = request.form['friend_name']
        new_number = request.form['phone_number']
        iD=friends_list[-1]['id']+1

        new_obj={
            'id':iD,
            'amount':new_amount,
            'friend_name':new_name,
            'phone_number':new_number,
        }
        split = new_amount/len(friends_list)
        for friend in friends_list:
            friend['amount'] = split
        friends_list.append(new_obj)
        return jsonify(friends_list),201


@app.route('/splitbill/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def update(id):
    if request.method == 'GET':
        for friend in friends_list:
            if friend['id'] == id:
                return jsonify(friend)
            pass
    if request.method == 'PUT':
        for friend in friends_list:
            if friend['id'] == id:
                friend['friend_name'] = request.form['friend_name']
 friend['amount'] = request.form['amount']
                friend['phone_number'] = request.form['phone_number']
                updated_list = {
                        'id': id,
                        'friend_name': friend['friend_name'],
                        'amount': friend['amount'],
                        'phone_number': friend['phone_number'],
                }
                return jsonify(updated_list)
    if request.method == 'DELETE':
        for index, friend in enumerate(friends_list):
            if friend['id'] == id:
                friends_list.pop(index)
                return jsonify(friends_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
-- INSERT --                                                                                                                        91,1          Bot

