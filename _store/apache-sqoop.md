---
aid: apache-sqoop
name: Apache Sqoop
description: 'Apache Sqoop is a command-line tool designed for efficiently transferring bulk data between Apache Hadoop and structured data stores such as relational databases. It supports parallel import and export of data, incremental loads, and direct database connectors for MySQL, PostgreSQL, Oracle, SQL Server, and DB2. Note: Apache Sqoop has been retired to the Apache Attic as of 2021. Users are encouraged to migrate to Apache Spark or Apache NiFi.'
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Big Data
  - Data Transfer
  - ETL
  - Hadoop
  - RDBMS
  - Retired
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-sqoop/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-sqoop:apache-sqoop-cli
    name: Apache Sqoop CLI
    description: Apache Sqoop provides a command-line interface for bulk data transfer between Hadoop and relational databases. Commands include sqoop-import for loading data into HDFS or Hive, sqoop-export for writing Hadoop data back to RDBMS, sqoop-job for managing saved jobs, and sqoop-eval for executing SQL statements. Sqoop 2 added a REST API server for job management.
    humanURL: https://sqoop.apache.org/docs/1.4.7/SqoopUserGuide.html
    tags:
      - CLI
      - Data Transfer
      - ETL
      - Hadoop
      - RDBMS
    properties:
      - type: Documentation
        url: https://sqoop.apache.org/docs/1.4.7/SqoopUserGuide.html
common:
  - type: GitHubRepository
    url: https://github.com/apache/sqoop
  - type: Documentation
    url: https://sqoop.apache.org/docs/1.4.7/
  - type: Portal
    url: https://sqoop.apache.org/
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Bulk Import
        description: High-throughput parallel import from RDBMS to HDFS, Hive, or HBase.
      - name: Bulk Export
        description: Export data from HDFS back to relational database tables.
      - name: Incremental Loads
        description: Delta-based incremental loading using append or lastmodified strategies.
      - name: Direct Import Mode
        description: Native database utility-based transfers for MySQL and PostgreSQL.
      - name: Hive Integration
        description: Auto-create Hive tables and load imported data directly into Hive.
  - type: UseCases
    data:
      - name: Data Warehouse Loading
        description: Load relational database data into Hadoop-based data warehouses.
      - name: Database Offloading
        description: Move historical data from RDBMS to HDFS for cost-effective storage.
  - type: Integrations
    data:
      - name: Apache Hadoop
        description: Primary target storage for Sqoop imports via HDFS.
      - name: Apache Hive
        description: Create and populate Hive tables from RDBMS imports.
      - name: MySQL
        description: MySQL JDBC and direct mysqldump-based connector.
      - name: Oracle
        description: Oracle JDBC connector for enterprise database data transfer.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
