<a name="README">[Riurik](https://github.com/andrew-malkov/Riurik)</a>
=======
**A web-based development framework for acceptance testing web applications.**

There are some great acceptence testing frameworks out there already, so why did we write another? Riurik aims to simplify the process of integration testing web applications. It's written in Javascript and Python using jQuery, Qunit, Django, heavily influenced by, and borrows the best parts of Fitnesse.

My two-year experience with using Fitnesse for testing web applications is that acceptance tests cost too much, since:

- You write acceptance tests in natural language using table-driven approach, that introduces additional complexity layer;
- You have to use tools like Selenium to test UI, that is one more complexity layer;
- Programming in Fitnesse has a steep learning curve and remains a nuisance due to its obsure syntax constructs;
- Fitnesse doesn't work with refactoring tools. Once you have a lot of tests, they become a real maintenance burden;

The planned benefit of tools like Fitnesse is that a business is supposed to be involved in writing examples, thus improving communication between customers and programmers. But in practice,  the business involvement for the acceptance tests is minimal or absent at all, whereas the added complexity of the extra Fitnesse layer is significant.

From my perspective organising a specification workshop much more viable approach. Getting project stakeholders in the same room, identifing functional gaps, clearing up inconsistencies and misunderstandings, discussing use cases, and resolving issues lead to writing down identifed examples and specifications which can be then converted to acceptance tests.

Like so you can eliminate first complexity layer and start to write acceptence tests using usual programming language. But not any language can help here. Acceptence tests for me are a live specification, i.e. a source of information on what goes on in my system. So they should be easy to read and understand in such a way as to help with handing over and taking over a code when issues happen or change requests come in later.
So this programming language should be expressive enough to write the tests in an easy-to-read and succinct way.