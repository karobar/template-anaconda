```
docker build -t template-anaconda .
docker run -w $PWD -v $PWD:$PWD template-anaconda
```