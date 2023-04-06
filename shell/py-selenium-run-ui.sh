#!/bin/bash
ENV=$1

if [ ! ${ENV} ]
then
    ENV=''
fi

export ATAS_CONF=${ENV}
#pytest -s /Users/tao.ding/PycharmProjects/atas-easy-test-py/testcase/auto-test/ --html=report.html
pytest -s /Users/tao.ding/PycharmProjects/atas-easy-test-py/testcase/api/ --html=report.html
echo 'This execution is completed!'
export ATAS_CONF=''