---
aid: database-schema-design
name: Database Schema Design
description: Database Schema Design is the practice of defining the tables, columns, data types, constraints, indexes, and relationships that make up a database. It applies to relational, document, key-value, columnar, and graph stores, and is supported by ER tooling, schema-as-code formats like DBML and Prisma, migration tools like Liquibase and Flyway, and emerging schema registries for streaming and document data.
type: Topic
xType: topic
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Modeling
  - Database
  - Database Schema Design
  - Schema Design
  - Software Architecture
created: '2025-01-01'
modified: '2026-04-30'
url: https://raw.githubusercontent.com/api-evangelist/database-schema-design/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis: []
common:
  - url: https://en.wikipedia.org/wiki/Database_schema
    name: Wikipedia
    type: Reference
    description: Wikipedia article on database schema concepts.
  - url: https://www.iso.org/standard/76583.html
    name: ISO/IEC 9075 (SQL)
    type: Standard
    description: International standard for SQL, including DDL for schema definition.
  - url: https://www.iso.org/standard/76586.html
    name: ISO/IEC 9075-11 (SQL Information Schema)
    type: Standard
    description: SQL standard for information and definition schemas.
  - url: https://www.dbml.org/
    name: DBML
    type: Reference
    description: Database Markup Language for declaring schemas as code.
  - url: https://www.prisma.io/docs/orm/prisma-schema
    name: Prisma Schema
    type: Tool
    description: Prisma's declarative schema language for application databases.
  - url: https://www.liquibase.org/
    name: Liquibase
    type: Tool
    description: Database schema change management and migration tool.
  - url: https://flywaydb.org/
    name: Flyway
    type: Tool
    description: Database migration tool with versioned SQL changes.
  - url: https://atlasgo.io/
    name: Atlas
    type: Tool
    description: Modern declarative schema-as-code platform for databases.
  - url: https://sqlmesh.com/
    name: SQLMesh
    type: Tool
    description: Data transformation and schema evolution platform.
  - url: https://erwin.com/
    name: erwin Data Modeler
    type: Tool
    description: Enterprise ER modeling and schema design tool.
  - url: https://dbdiagram.io/
    name: dbdiagram.io
    type: Tool
    description: Web-based ERD tool that uses DBML.
  - url: https://www.lucidchart.com/pages/database-diagram/database-design
    name: Lucidchart Database Design
    type: Reference
    description: Lucidchart guide to database design and ERDs.
  - url: https://docs.confluent.io/platform/current/schema-registry/index.html
    name: Confluent Schema Registry
    type: Tool
    description: Schema registry for Avro, JSON Schema, and Protobuf in streaming pipelines.
  - url: https://www.mongodb.com/docs/manual/data-modeling/
    name: MongoDB Data Modeling
    type: Reference
    description: MongoDB schema design guide for document databases.
  - url: vocabulary/database-schema-design-vocabulary.yml
    name: Vocabulary
    type: Vocabulary
    description: Vocabulary of database schema design concepts.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
