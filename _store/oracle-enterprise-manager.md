---
aid: oracle-enterprise-manager
url: https://raw.githubusercontent.com/api-evangelist/oracle-enterprise-manager/refs/heads/main/apis.yml
apis:
- name: Oracle Enterprise Manager Cloud Control REST API
  description: REST API for Oracle Enterprise Manager Cloud Control providing access to monitoring, configuration, and administration capabilities including targets, metrics, incidents, blackouts, credentials, user management, and deployment procedures.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/APIOverview.html
  baseURL: https://<em-host>:<port>/em/api
  tags:
  - Administration
  - Cloud Control
  - Monitoring
  - REST API
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/APIOverview.html
  - type: OpenAPI
    url: openapi/oracle-enterprise-manager-cloud-control-openapi.yml
  - type: JSONSchema
    url: json-schema/oracle-enterprise-manager-target-schema.json
  - type: JSONLD
    url: json-ld/oracle-enterprise-manager-context.jsonld
  - type: Authentication
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/Authentication.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: Getting Started
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/SendRequests.html
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://www.oracle.com/support/
- name: Enterprise Manager Command Line Interface (EM CLI)
  description: Command-line interface providing scriptable access to Enterprise Manager functionality including target management, job operations, patching, provisioning, and administration tasks through verbs that can be used in shell scripts, Perl, and Python.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emcli/
  baseURL: https://<em-host>:<port>/em
  tags:
  - Automation
  - CLI
  - Command Line
  - Scripting
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emcli/
  - type: Getting Started
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emcli/getting-started-em-cli.html
  - type: Command Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emcli/em-cli-verbs.html
  - type: Authentication
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emcli/emcli-security.html
- name: Enterprise Manager Job System API
  description: API for creating, managing, and monitoring Enterprise Manager jobs and tasks including scheduling, execution tracking, and deployment procedures.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/websvcs/restful/emws/job
  tags:
  - Automation
  - Jobs
  - Scheduling
  - Task Management
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
- name: Enterprise Manager Metric and Monitoring API
  description: API for accessing performance metrics, monitoring data, and alerting information including numeric metric data points over time, latest metric values, and metric group metadata.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/websvcs/restful/emws/metric
  tags:
  - Alerts
  - Metrics
  - Monitoring
  - Performance
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: Monitoring Guide
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emmon/executing-sql-rest-api.html
- name: Enterprise Manager Target Management API
  description: API for managing monitored targets including discovery, configuration, lifecycle operations, bulk property updates, and target type metadata.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/websvcs/restful/emws/target
  tags:
  - Configuration
  - Discovery
  - Lifecycle
  - Target Management
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
- name: Enterprise Manager Incidents and Events API
  description: REST API for searching, viewing, and managing incidents and events in Enterprise Manager, including clearing, suppressing, unsuppressing incidents, viewing member events, and managing annotations.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/api/incidents
  tags:
  - Alerting
  - Events
  - Incidents
  - Troubleshooting
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
- name: Enterprise Manager Blackout Management API
  description: REST API for managing blackouts (maintenance windows) in Enterprise Manager, including creating, editing, deleting, listing, and stopping blackouts, managing blackout reasons, and retrieving targets in blackouts.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/api/blackouts
  tags:
  - Blackouts
  - Maintenance Windows
  - Scheduling
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
- name: Enterprise Manager Credentials Management API
  description: REST API for managing named credentials, monitoring credentials, and preferred credentials in Enterprise Manager, including creating, listing, deleting, updating, testing, and searching credential types.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/api/credentials
  tags:
  - Authentication
  - Credentials
  - Security
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: Security Guide
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emsec/index.html
- name: Enterprise Manager User Management API
  description: REST API for managing Enterprise Manager users and roles, including creating, modifying, and deleting users and roles, managing privilege grants and role assignments, and listing secure resources and permissions.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/api/users
  tags:
  - Permissions
  - Roles
  - Security
  - User Management
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: Security Guide
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emsec/index.html
- name: Enterprise Manager Database Patching and Maintenance API
  description: REST API for database maintenance operations including updates, upgrades, and patching, with support for creating and managing Gold Images, patch recommendations, compliance reporting, and Fleet Patching and Provisioning (FPP) integration.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emlcm/patch-history.html
  baseURL: https://<em-host>:<port>/em/api/dblm
  tags:
  - Database Maintenance
  - Fleet Maintenance
  - Gold Images
  - Lifecycle Management
  - Patching
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emlcm/patch-history.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: Fleet Patching Guide
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emlcm/fleet-maintenance-patching-fpp.html
- name: Enterprise Manager Deployment Procedure API
  description: REST API for managing deployment procedures including creating, submitting, and deleting procedures, managing procedure instances with resume, suspend, stop, and retry operations, and tracking execution history.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/api/deploymentProcedures
  tags:
  - Automation
  - Deployment
  - Procedures
  - Provisioning
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
- name: Enterprise Manager Database Backup Management API
  description: REST API for configuring and managing database backup settings, fleet-level backup configuration, and scheduling backup operations in Enterprise Manager.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/api/databaseBackup
  tags:
  - Backup Management
  - Database Backup
  - Recovery
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
- name: Enterprise Manager ZDLRA Management API
  description: REST API for managing Oracle Zero Data Loss Recovery Appliance (ZDLRA) including adding and removing protected databases, creating and managing protection policies, creating archival backups, and retrieving restore information.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  baseURL: https://<em-host>:<port>/em/api/zdlra
  tags:
  - Data Protection
  - Recovery Appliance
  - ZDLRA
  - Zero Data Loss
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
- name: Enterprise Manager SQL Execution REST API
  description: REST API for executing SQL queries against database targets monitored by Enterprise Manager and against the Enterprise Manager repository, enabling custom data extraction for dashboards and KPI reports.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emmon/executing-sql-rest-api.html
  baseURL: https://<em-host>:<port>/em/api/db/sql
  tags:
  - Data Extraction
  - Database Queries
  - Reporting
  - SQL Execution
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emmon/executing-sql-rest-api.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrest/rest-endpoints.html
- name: Enterprise Manager Data Guard Administration REST API
  description: REST API for managing Oracle Data Guard configurations in Enterprise Manager, enabling high availability operations including switchover, failover, and standby database management.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emlcm/data-guard-administration-rest-api1.html
  baseURL: https://<em-host>:<port>/em/api/dataguard
  tags:
  - Data Guard
  - Disaster Recovery
  - High Availability
  - Standby Database
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emlcm/data-guard-administration-rest-api1.html
  - type: Lifecycle Management Guide
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emlcm/patch-history.html
- name: Enterprise Manager Cloud APIs (DBaaS)
  description: REST APIs for Database as a Service (DBaaS) operations enabling self-service database provisioning, request management, and quota administration through Enterprise Manager Cloud Control.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.4/emclo/using-cloud-apis.html
  baseURL: https://<em-host>:<port>/em/cloud
  tags:
  - Cloud
  - Database as a Service
  - DBaaS
  - Provisioning
  - Self-Service
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.4/emclo/using-cloud-apis.html
  - type: API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.4/emclo/database-service-ssa-user-rest-apis.html
  - type: Administrator API Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.4/emclo/database-service-administrator-rest-apis.html
  - type: Use Cases
    url: https://docs.oracle.com/cd/E73210_01/EMCLO/GUID-99E7450E-4255-46B5-9C0E-DC520DE376D2.htm
- name: Enterprise Manager Extensibility Development Kit (EDK) API
  description: Extensibility Development Kit providing tools, utilities, and APIs for developing Enterprise Manager plug-ins to extend platform capabilities for custom target monitoring and management.
  image: https://www.oracle.com/a/ocom/img/oracle-enterprise-manager.jpg
  humanURL: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/plug-ins.html
  baseURL: https://<em-host>:<port>/em
  tags:
  - Custom Monitoring
  - Extensibility
  - Plugin Development
  - SDK
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/plug-ins.html
  - type: Programmers Guide
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.4/emprg/getting-started-enterprise-manager-plug-ins.html
  - type: Programmers Reference
    url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.4/emprf/getting-started-plug-development.html
name: Oracle Enterprise Manager
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Oracle Enterprise Manager (OEM) provides a comprehensive management platform for managing Oracle IT infrastructure and applications. The APIs enable programmatic access to monitoring, administration, and automation capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

