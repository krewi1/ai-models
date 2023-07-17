FROM python
WORKDIR /app
RUN pip install -U insightface
RUN apt update
RUN apt install vim -y
RUN wget -P /root./.insightface/models https://huggingface.co/deepinsight/inswapper/resolve/main/inswapper_128.onnx
RUN wget -P /root/.insightface/models https://github.com/deepinsight/insightface/releases/download/v0.7/buffalo_l.zip
RUN unzip /root/.insightface/models/buffalo_l.zip -d /root/.insightface/models/buffalo_l
RUN pip install onnxruntime
COPY entrypoint/entrypoint.py /app/main.py


ENTRYPOINT ["python", "main.py"]
