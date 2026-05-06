---
aid: database-normalization
name: Database Normalization
description: Database Normalization is the formal process of structuring relational schemas to reduce redundancy and avoid update, insert, and delete anomalies. It is governed by Codd's normal forms (1NF through 6NF) and the Boyce-Codd Normal Form, and is the foundation of relational design, taught in academic curricula and applied across all major SQL databases.
type: Topic
xType: topic
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Database Design
  - Database Normalization
  - Normal Forms
  - Relational Theory
  - Schema Design
created: '2025-01-01'
modified: '2026-04-30'
url: https://raw.githubusercontent.com/api-evangelist/database-normalization/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis: []
common:
  - url: https://en.wikipedia.org/wiki/Database_normalization
    name: Wikipedia
    type: Reference
    description: Wikipedia article on database normalization.
  - url: https://en.wikipedia.org/wiki/First_normal_form
    name: First Normal Form
    type: Reference
    description: Definition of 1NF requiring atomic values and no repeating groups.
  - url: https://en.wikipedia.org/wiki/Second_normal_form
    name: Second Normal Form
    type: Reference
    description: Definition of 2NF removing partial dependencies on composite keys.
  - url: https://en.wikipedia.org/wiki/Third_normal_form
    name: Third Normal Form
    type: Reference
    description: Definition of 3NF removing transitive dependencies.
  - url: https://en.wikipedia.org/wiki/Boyce%E2%80%93Codd_normal_form
    name: Boyce-Codd Normal Form
    type: Reference
    description: BCNF, a stricter variant of 3NF.
  - url: https://en.wikipedia.org/wiki/Fourth_normal_form
    name: Fourth Normal Form
    type: Reference
    description: 4NF eliminating multi-valued dependencies.
  - url: https://en.wikipedia.org/wiki/Fifth_normal_form
    name: Fifth Normal Form
    type: Reference
    description: 5NF eliminating join dependencies.
  - url: https://en.wikipedia.org/wiki/Sixth_normal_form
    name: Sixth Normal Form
    type: Reference
    description: 6NF for temporal databases with full decomposition.
  - url: https://en.wikipedia.org/wiki/Domain-key_normal_form
    name: Domain-Key Normal Form
    type: Reference
    description: DKNF, a normal form that prevents all anomalies.
  - url: https://en.wikipedia.org/wiki/Functional_dependency
    name: Functional Dependency
    type: Reference
    description: Foundational concept underlying normalization.
  - url: https://www.acm.org/binaries/content/assets/publications/computing-classics/codd-relational-model.pdf
    name: Codd 1970 Paper
    type: Reference
    description: E.F. Codd's foundational paper on the relational model.
  - url: https://www.iso.org/standard/76583.html
    name: ISO/IEC 9075 (SQL)
    type: Standard
    description: ISO standard for SQL, the language used to implement normalized schemas.
  - url: vocabulary/database-normalization-vocabulary.yml
    name: Vocabulary
    type: Vocabulary
    description: Vocabulary of database normalization concepts and normal forms.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
