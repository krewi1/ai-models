# Face swap AI

It is using [insightface](https://github.com/deepinsight/insightface) behind the scene

## Usage

First create directory `out` in current directory. It will be used to store temporary files and final result.
To use faces from image `source_image.jpg` to replace faces in image `target_image.jpg` use following command:

```bash
docker run -it --rm -v $(pwd)/source_image.jpg:/app/source.jpg -v $(pwd)/target_image.jpg:/app/target.jpg -v $(pwd)/out:/app/out krewi/deepinsight -s source.jpg -t target.jpg -o out/out-0.jpg
```

It is using faces from source_image from left to right. If you want to start from different face then first one, use `-i` flag like this:

```bash
docker run -it --rm -v $(pwd)/source_image.jpg:/app/source.jpg -v $(pwd)/target_image.jpg:/app/target.jpg -v $(pwd)/out:/app/out krewi/deepinsight -s source.jpg -t target.jpg -i 1 -o out/out-1`.jpg
```
