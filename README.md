**Introduction:**
POM(Page Object Model) is a design pattern that makes it easier to maintain our code and reduce code duplication.
It allows to abstract any page related information away from actual tests.
The selectors that are within tests, can be extracted and put it in a separate file which we can then reuse whenever we want.
**Advantages**
Code separation – Keep test and locators separately, makes our code clean, easy to understand, and maintain
Single source of the repository – all the locators are stored in one place. Tests become short and optimized as we can reuse locators and page object methods
Readability – improves significantly and makes it easy for new team members to start writing tests by following the existing structure

