# Thailand-Holiday
Backend lambda project for managing photos

# How to Run
```
working dir should be /thai_holiday/packages
rm -rf build/lambdas
cp -r services/lambdas/ build/lambdas/
python3 -m pip install -r build/lambdas/api/requirements.txt --target build/lambdas
cd build/lambdas/
zip -r lambdas.zip . -x "*README.md" "*requirements.txt"
```
Then copy lambdas.zip into the lambda function code in AWS
TODO - put these steps into an automated pipeline. Fat chance!