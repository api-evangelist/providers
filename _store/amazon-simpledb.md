---
aid: amazon-simpledb
name: Amazon SimpleDB
description: Amazon SimpleDB is a highly available NoSQL data store that offloads the work of database administration. It provides simple and powerful data storage and querying capabilities to enable you to build web applications with structured data storage without the overhead of database administration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Cloud Storage
  - Data Storage
  - Database
  - NoSQL
url: https://raw.githubusercontent.com/api-evangelist/amazon-simpledb/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-simpledb:amazon-simpledb-api
    name: Amazon SimpleDB API
    description: The Amazon SimpleDB API provides programmatic access to create and manage domains, items, and attributes for simple NoSQL data storage and querying of structured data in the cloud.
    humanURL: https://aws.amazon.com/simpledb/
    baseURL: https://sdb.amazonaws.com
    tags:
      - Data Storage
      - Database
      - NoSQL
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-simpledb.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/simpledb/
      - type: Pricing
        url: https://aws.amazon.com/simpledb/pricing/
      - type: FAQ
        url: https://aws.amazon.com/simpledb/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/simpledb/
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Welcome.html
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/database/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/simpledb/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-simpledb-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-simpledb-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-simpledb.yaml
  - type: Features
    data:
      - name: Simple Data Storage
        description: NoSQL data store with no database administration overhead.
      - name: Schema-less
        description: Store structured data without a predefined schema.
      - name: High Availability
        description: Automatically replicated data across multiple availability zones.
      - name: Select Query Language
        description: Query data using a simple SELECT expression language.
  - type: UseCases
    data:
      - name: Web Application Data Storage
        description: Store and query structured data for web applications.
      - name: User Profile Storage
        description: Store user attributes and preferences without schema management.
      - name: Metadata Storage
        description: Store metadata for files, media, or other cloud resources.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store metadata for S3 objects in SimpleDB.
      - name: Amazon EC2
        description: Store instance metadata and configuration in SimpleDB.
      - name: AWS CloudTrail
        description: Audit SimpleDB API calls via CloudTrail.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
x-type: company
---
