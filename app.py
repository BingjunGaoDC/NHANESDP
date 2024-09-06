from flask import Flask, request, jsonify # type: ignore
import joblib

import joblib
import os

# 获取当前文件所在的目录路径
current_dir = os.path.dirname(__file__)

# 加载模型，使用相对路径
model_path = os.path.join(current_dir, 'model.pkl')
model = joblib.load(model_path)


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # 获取数据，假设数据是以 JSON 格式发送，包含八个连续型变量
    data = request.json
    
    # 从数据中提取对应的变量值 (ap, crp, ca, ggt, tp, ab, gc, nab)
    input_data = [
        data['ap'],  # 碱性磷酸酶 (ap)
        data['crp'], # C反应蛋白 (crp)
        data['ca'],  # 钙 (ca)
        data['ggt'], # γ-谷氨酰转移酶 (ggt)
        data['tp'],  # 总蛋白 (tp)
        data['ab'],  # 白蛋白 (ab)
        data['gc'],  # 血糖 (gc)
        data['nab']  # 非白蛋白 (nab)
    ]
    
    # 使用模型进行预测
    prediction = model.predict([input_data])
    
    # 返回预测结果
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
