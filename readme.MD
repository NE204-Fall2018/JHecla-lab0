# NE 204 lab 0

To get data:
make data

To get analysis
make analysis

To test
make test

## How to use this template

[H/T stack overflow](https://stackoverflow.com/questions/1657017/how-to-squash-all-git-commits-into-one/9254257#9254257)

```bash
# Create a new directory for your report
mkdir my_lab_report && cd $_
# Create an empty repository
git init
# Initialize the repo with the template
git fetch --depth=1 -n https://github.com/NE204-Spring2018/lab_report_template.git
git reset --hard $(git commit-tree FETCH_HEAD^{tree} -m "initial commit")
```
