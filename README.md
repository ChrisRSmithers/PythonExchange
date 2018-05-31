# Python Exchange

An experiment into combining a ForEx API along with Tensorflow for singal processing. The goal is to achieve a model which predicts the correct time to make exchanges between two currencies given that certain levels of exchange need to be met. Initially, we aim to use the Quandl API for foreign exchange rates, both current and historical. Eventually the aim is to have a full system deployed to AWS, sending emails to a user as and when exchanges should occur

## The problem

Suppose one is required to make regular transactions from currency A to currency B. For example, suppose money is earned at some rate *r* in currency A, but that every month, some fixed amount needs to be paid in currency B. The goal is to minimise the amount of expected expenditure in currency A in order to meet the required spending in currency B.

## Authors

* **Chris Smithersn**