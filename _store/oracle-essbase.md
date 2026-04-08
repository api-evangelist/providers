---
aid: oracle-essbase
url: https://raw.githubusercontent.com/api-evangelist/oracle-essbase/refs/heads/main/apis.yml
apis:
- name: Oracle Essbase REST API
  description: RESTful API for managing and interacting with Oracle Essbase applications, databases, and performing analytical operations. Enables automation of Essbase resource management with endpoints for applications, databases, calculations, data loads, and user management.
  image: https://www.oracle.com/a/ocom/img/oracle-essbase.jpg
  humanURL: https://docs.oracle.com/en/database/other-databases/essbase/21/essrt/index.html
  baseURL: https://{host}:{port}/essbase/rest/v1
  tags:
  - Analytics
  - Calculations
  - Data Management
  - OLAP
  - REST API
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/other-databases/essbase/21/essrt/index.html
  - type: OpenAPI
    url: openapi/oracle-essbase-rest-api-openapi.yml
  - type: Authentication
    url: https://docs.oracle.com/en/database/other-databases/essbase/21/erest/op-rest-v1-sessions-post.html
  - type: Reference
    url: https://docs.oracle.com/en/database/other-databases/essbase/21/essrt/rest-endpoints.html
  - type: Getting Started
    url: https://docs.oracle.com/en/database/other-databases/essbase/21/essrt/api-essbase.html
  - type: JSON Schema
    url: json-schema/oracle-essbase-application-schema.json
  - type: JSON Schema
    url: json-schema/oracle-essbase-database-schema.json
  - type: JSON Schema
    url: json-schema/oracle-essbase-job-schema.json
  - type: JSON Schema
    url: json-schema/oracle-essbase-user-schema.json
  - type: JSON Schema
    url: json-schema/oracle-essbase-session-schema.json
  - type: JSON Schema
    url: json-schema/oracle-essbase-dimension-schema.json
  - type: JSON Schema
    url: json-schema/oracle-essbase-connection-schema.json
  - type: JSON Schema
    url: json-schema/oracle-essbase-script-schema.json
  - type: JSON Schema
    url: json-schema/oracle-essbase-filter-schema.json
  - type: JSON-LD Context
    url: json-ld/oracle-essbase-context.jsonld
  contact:
  - FN: Oracle Support
    url: https://support.oracle.com
- name: Essbase Java API
  description: Java API for developing applications that interact with Oracle Essbase for data loading, calculations, and retrievals. Provides libraries, samples, and documentation for building Essbase client tools in Java.
  humanURL: https://docs.oracle.com/en/database/other-databases/essbase/21/esjav/
  tags:
  - Client Tools
  - Data Loading
  - Java
  - Programming Interface
  - SDK
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/other-databases/essbase/21/esjav/
- name: Essbase C API
  description: C API for building high-performance applications that interact with Essbase databases. Includes the Grid API for Smart View-like functionality and the Outline API for programmatic outline manipulation.
  humanURL: https://docs.oracle.com/en/database/other-databases/essbase/21/esoac/
  tags:
  - C API
  - Grid API
  - Native Interface
  - Outline API
  - SDK
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/other-databases/essbase/21/esoac/
- name: Essbase MaxL Scripting Interface
  description: MaxL is the multi-dimensional database access language for Essbase that provides a scripting-based interface for administering and querying Essbase. It enables automation of administrative operations using statements rather than a series of commands.
  humanURL: https://docs.oracle.com/en/database/other-databases/essbase/21/esssr/maxl.html
  tags:
  - Administration
  - Automation
  - Database Management
  - Query Language
  - Scripting
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/other-databases/essbase/21/esssr/maxl.html
  - type: Authentication
    url: https://docs.oracle.com/en/database/other-databases/essbase/21/esssr/login-logout-cli-authentication.html
- name: Essbase CLI (Command Line Interface)
  description: Command-line interface for administering and managing Essbase applications and databases. Provides command-line access for common administrative tasks including application management, data operations, and server configuration.
  humanURL: https://docs.oracle.com/en/database/other-databases/essbase/21/essug/
  tags:
  - Administration
  - Automation
  - CLI
  - Command Line
  - Server Management
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/other-databases/essbase/21/essug/
name: Oracle Essbase
tags:
- Analytics
- Budgeting
- Business Intelligence
- Financial Consolidation
- Multi-Dimensional Database
- OLAP
- Planning
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Oracle Essbase is a multi-dimensional database management system that provides a multidimensional analytical platform for business intelligence applications, financial consolidation, planning, budgeting, and forecasting.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

