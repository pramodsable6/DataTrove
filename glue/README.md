Docker command to launch jupyter lab for local Glue ETL development -
```shell
docker run -it -v ~/.aws:/home/glue_user/.aws -p 8888:8888 -p 4040:4040 -e AWS_PROFILE=dev -e DISABLE_SSL="true" --name glue_jupyter amazon/aws-glue-libs:glue_libs_4.0.0_image_01 /home/glue_user/jupyter/jupyter_start.sh
```
