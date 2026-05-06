---
aid: oracle-planning
name: Oracle Planning
description: A collection of APIs for Oracle Planning and Budgeting Cloud Service (PBCS) and Enterprise Performance Management (EPM) Planning. Oracle EPM Cloud provides REST APIs across planning, budgeting, forecasting, financial consolidation, account reconciliation, tax reporting, narrative reporting, profitability and cost management, and enterprise data management services.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-planning/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
apis:
  - name: Oracle Planning REST API
    description: RESTful API for Oracle Planning and Budgeting Cloud Service providing access to planning applications, data, and metadata. Use the Planning REST APIs to manage and execute jobs, work with members, applications, planning units, user preferences, data slices, substitution variables, and user variables.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/index.html
    baseURL: https://{serviceHost}/HyperionPlanning/rest
    tags:
      - Budgeting
      - Cloud
      - EPM
      - Forecasting
      - Planning
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/rest/index.html
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/rest/openapi.json
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/rest/Authentication.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/planning_rest_apis.html
      - type: Getting Started
        url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/planning-tutorial-get-started/index.html
      - type: Tutorials
        url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/tutorials.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EPM Automate
    description: Command-line utility for automating Oracle EPM Cloud administration tasks. EPM Automate enables service administrators to remotely perform tasks including importing and exporting metadata, data, artifact and application snapshots, uploading and managing files, and downloading reports.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/cepma/using_epmctl.html
    baseURL: https://{serviceHost}
    tags:
      - Administration
      - Automation
      - CLI
      - EPM
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/cepma/using_epmctl.html
      - type: Downloads
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/epmat/epm_auto_download_utility.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Planning Smart View API
    description: API for integrating Oracle Smart View for Office with Oracle Planning applications. Smart View provides a common Microsoft Office interface for EPM products, allowing users to view, import, manipulate, distribute, and share data in Excel, Word, and PowerPoint.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/svuga/index.html
    baseURL: https://{serviceHost}
    tags:
      - Excel
      - Office Integration
      - Reporting
      - Smart View
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/svuga/index.html
      - type: User Guide
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/svpbc/launch.html
      - type: Developer Guide
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/svdvg/
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Planning Data Management API
    description: REST API for data integration and management in Oracle Planning applications. Provides endpoints for running data rules, integrations, and pipelines, as well as importing and exporting data snapshots and managing point-of-view lock and unlock operations.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/dpbcs/index.html
    baseURL: https://{serviceHost}/aif/rest
    tags:
      - Data Load
      - Data Management
      - ETL
      - Integration
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/dpbcs/index.html
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/rest/op-aif-rest-v1-datamanagement-jobs-post.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EPM Migration REST API
    description: REST API for lifecycle management and migration operations in Oracle EPM Cloud. Provides endpoints for managing application snapshots, importing and exporting artifacts, managing files and object storage, performing SFTP operations, and exporting Essbase data.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
    baseURL: https://{serviceHost}/interop/rest
    tags:
      - Backup
      - Lifecycle Management
      - Migration
      - Snapshots
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/quick_reference_table_rest_api_resource_view.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EPM Security REST API
    description: REST API for managing users, groups, and roles in Oracle EPM Cloud environments. Provides endpoints for user and group administration, role assignment, restricted data access control, encryption key management, and security configuration.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
    baseURL: https://{serviceHost}/interop/rest/security
    tags:
      - Groups
      - Roles
      - Security
      - Users
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/quick_reference_table_rest_api_resource_view.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Financial Consolidation and Close REST API
    description: REST API for Oracle Financial Consolidation and Close Cloud Service (FCCS). Provides endpoints for retrieving and managing journals, submitting, approving, posting, and rejecting journals, updating journal periods, importing supplementation data, copying and clearing data, and deploying form templates.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/index.html
    baseURL: https://{serviceHost}/HyperionPlanning/rest
    tags:
      - Close Management
      - Eliminations
      - Financial Consolidation
      - Journals
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/epm-cloud/prest/fccs_chapter_intro.html
      - type: Integration Guide
        url: https://docs.oracle.com/en/cloud/saas/epm-cloud/intgr/fccs_integrate_with_rest.html
      - type: Tutorials
        url: https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/tutorials.html
      - type: Training
        url: https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/training.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Account Reconciliation REST API
    description: REST API for Oracle Account Reconciliation Cloud Service (ARCS). Provides endpoints for creating reconciliations, changing period status, importing pre-mapped transactions, importing profiles, importing currency rates, importing balances, monitoring reconciliations, and retrieving job status. Also supports Transaction Matching for importing and auto-matching transactions.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/
    baseURL: https://{serviceHost}/armARCS/rest
    tags:
      - Account Reconciliation
      - Compliance
      - Financial Close
      - Transaction Matching
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/arcs_chapter_intro.html
      - type: Integration Guide
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/intgr/arcs_integrate_with_rest.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Tax Reporting REST API
    description: REST API for Oracle Tax Reporting Cloud Service. Provides endpoints for retrieving the REST API version, importing supplementation data, copying data, clearing data, and deploying form templates for tax provisioning and reporting workflows.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/tax-reporting-cloud/index.html
    baseURL: https://{serviceHost}/HyperionPlanning/rest
    tags:
      - Compliance
      - EPM
      - Tax Provisioning
      - Tax Reporting
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/tax_reporting_chapter_intro.html
      - type: Integration Guide
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/intgr/trcs_integrate_with_rest.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Narrative Reporting REST API
    description: REST API for Oracle Narrative Reporting Cloud Service. Provides endpoints for managing report artifacts, bursting definitions, files, and jobs. Allows downloading files, uploading temporary files, starting asynchronous jobs, and managing library artifacts for management and regulatory reporting.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-performance-reporting-cloud/
    baseURL: https://{serviceHost}/epm/rest
    tags:
      - EPM
      - Management Reporting
      - Narrative Reporting
      - Reports
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/eprcs_chapter_intro.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-reporting-cloud/raepr/rest-endpoints.html
      - type: Integration Guide
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/intgr/eprcs_integrate_with_rest.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Enterprise Profitability and Cost Management REST API
    description: REST API for Oracle Enterprise Profitability and Cost Management Cloud Service. Provides endpoints for model calculation, data operations, and managing profitability models used to compute cost and revenue allocations for business profitability analysis.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-profitability-cost-management-cloud/
    baseURL: https://{serviceHost}/HyperionPlanning/rest/v3
    tags:
      - Allocations
      - Cost Management
      - EPM
      - Profitability
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
      - type: Integration Guide
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/intgr/pcmcs_get_started_topicmap.html
      - type: Training
        url: https://docs.oracle.com/en/cloud/saas/enterprise-profitability-cost-management-cloud/training.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Profitability and Cost Management REST API
    description: REST API for the classic Oracle Profitability and Cost Management Cloud Service. Provides endpoints for managing data grants, point-of-view operations, query exports, and file-based application management for cost allocation and profitability analysis.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/profit-cost-cloud/index.html
    baseURL: https://{serviceHost}/epm/rest
    tags:
      - Cost Allocation
      - Cost Management
      - EPM
      - Profitability
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle FreeForm REST API
    description: REST API for Oracle FreeForm Cloud Service. FreeForm provides a flexible EPM application building environment using the same Planning REST APIs for job management, member operations, planning units, substitution variables, and data slices without predefined module constraints.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/freeform/platform.html
    baseURL: https://{serviceHost}/HyperionPlanning/rest
    tags:
      - EPM
      - Flexible Modeling
      - FreeForm
      - Planning
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/planning_rest_apis.html
      - type: Integration Guide
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/intgr/freeform_get_started_topicmap.html
      - type: Training
        url: https://docs.oracle.com/en/cloud/saas/freeform/training.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Enterprise Data Management REST API
    description: REST API for Oracle Enterprise Data Management Cloud Service. Provides endpoints for managing applications, files, jobs, requests, views, dimensions, viewpoints, and system settings. Enables programmatic access to master data governance and data management operations.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-data-management-cloud/admin_use.html
    baseURL: https://{serviceHost}/epm/rest
    tags:
      - Data Governance
      - Enterprise Data Management
      - EPM
      - Master Data
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-data-management-cloud/edmra/edmcs_restapi_overview.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-data-management-cloud/edmra/rest-endpoints.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EPM Task Manager REST API
    description: REST API for Oracle EPM Task Manager. Provides endpoints for managing task status, deploying templates, and managing Oracle Integration Cloud connections within the financial close process and other EPM workflows.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
    baseURL: https://{serviceHost}/HyperionPlanning/rest/cmapi
    tags:
      - Close Management
      - EPM
      - Task Manager
      - Workflow
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/quick_reference_table_rest_api_resource_view.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EPM Enterprise Journals REST API
    description: REST API for Oracle EPM Enterprise Journals. Provides endpoints for executing journal jobs and retrieving and managing enterprise journal entries across EPM Cloud services for cross-application journal management and reporting.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
    baseURL: https://{serviceHost}/HyperionPlanning/rest/ej
    tags:
      - Enterprise Journals
      - EPM
      - Financial Close
      - Journals
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/quick_reference_table_rest_api_resource_view.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle EPM Groovy Scripting API
    description: Java-based scripting API for Oracle EPM Cloud that enables Groovy scripts to perform operations against the EPM object model. Allows dynamic generation of calculation scripts at runtime, validation checks for runtime prompts, data validation before form submissions, and integration with internal and external REST APIs.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.png
    humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/groov/oracle/epm/api/model/package-summary.html
    baseURL: https://{serviceHost}
    tags:
      - Business Rules
      - Calculation
      - Groovy
      - Scripting
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/groov/oracle/epm/api/model/package-summary.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/ecalc/groovy_java_api_reference.html
      - type: Getting Started
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/groovy-tutorial-introduction/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Budgeting
  - Cloud
  - Consolidation
  - Enterprise
  - EPM
  - Financial Close
  - Financial Planning
  - Forecasting
  - Oracle
  - Planning
include:
  - name: Oracle EPM Cloud Documentation
    url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/index.html
  - name: Oracle Cloud
    url: https://www.oracle.com/cloud/
common:
  - type: Portal
    url: https://cloud.oracle.com
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/index.html
  - type: Getting Started
    url: https://docs.oracle.com/en/cloud/saas/epm-cloud/
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/about_the_rest_api_for_cloud_plan_budget_guide.html
  - type: Reference
    url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/quick_reference_table_rest_api_resource_view.html
  - type: Change Log
    url: https://docs.oracle.com/en/cloud/saas/readiness/epm.html
  - type: Training
    url: https://docs.oracle.com/en/cloud/saas/epm-cloud/training.html
  - type: Tutorials
    url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/tutorials.html
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms.html
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
  - type: Support
    url: https://support.oracle.com
  - type: Status
    url: https://ocistatus.oraclecloud.com/
  - type: Blog
    url: https://blogs.oracle.com/proactivesupportepm/
  - type: Community
    url: https://community.oracle.com/customerconnect/categories/epm-epm-platform
  - type: Website
    url: https://www.oracle.com/performance-management/
  - type: Login
    url: https://cloud.oracle.com
  - type: Sign Up
    url: https://www.oracle.com/cloud/free/
  - type: GitHub Organization
    url: https://github.com/oracle
---
