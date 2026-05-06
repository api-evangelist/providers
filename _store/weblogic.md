---
name: Oracle WebLogic Server APIs
description: Collection of APIs and resources for Oracle WebLogic Server administration and management. WebLogic Server is Oracle's enterprise-grade Java EE application server providing high availability, scalability, and comprehensive management capabilities through RESTful management APIs, monitoring and diagnostics, and deployment services.
image: https://www.oracle.com/a/ocom/img/weblogic-server.png
url: https://www.oracle.com/middleware/technologies/weblogic.html
created: '2024'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - name: WebLogic RESTful Management Services API
    description: RESTful API for monitoring and managing WebLogic Server domains, servers, applications, and resources. Provides access to configuration editing, server lifecycle management, cluster administration, data source management, and JMS resource configuration.
    image: https://www.oracle.com/a/ocom/img/weblogic-server.png
    humanUrl: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/restm/
    baseUrl: https://host:port/management/weblogic/latest
    tags:
      - Administration
      - Clusters
      - Configuration
      - Data Sources
      - JMS
      - Management
      - Monitoring
      - REST
      - Server Lifecycle
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/restm/
      - type: OpenAPI
        url: openapi/weblogic-restful-management-services-openapi.yml
      - type: JSONSchema
        url: json-schema/weblogic-server-configuration.json
      - type: JSONSchema
        url: json-schema/weblogic-domain-configuration.json
      - type: JSONSchema
        url: json-schema/weblogic-cluster-configuration.json
      - type: JSONSchema
        url: json-schema/weblogic-datasource-configuration.json
      - type: JSONSchema
        url: json-schema/weblogic-server-runtime.json
      - type: JSONStructure
        url: json-structure/weblogic-server-configuration-structure.json
      - type: JSONLD
        url: json-ld/weblogic-context.jsonld
    contact:
      - FN: Oracle Support
        url: https://support.oracle.com
  - name: WebLogic Monitoring and Diagnostics API
    description: API for accessing runtime monitoring data, metrics, and diagnostics information. Provides server health, JVM metrics, thread pool statistics, JDBC data source metrics, JMS statistics, application deployment metrics, and WLDF diagnostics.
    humanUrl: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlrst/
    baseUrl: https://host:port/management/wls/latest
    tags:
      - Diagnostics
      - Health
      - JMX
      - Metrics
      - Monitoring
      - Performance
      - WLDF
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlrst/
      - type: OpenAPI
        url: openapi/weblogic-monitoring-diagnostics-openapi.yml
      - type: JSONSchema
        url: json-schema/weblogic-server-runtime.json
      - type: JSONLD
        url: json-ld/weblogic-context.jsonld
  - name: WebLogic Deployment API
    description: API for deploying, undeploying, redeploying, and managing applications and shared libraries. Supports the full deployment lifecycle including prepare, activate, start, stop, redeploy, and undeploy operations.
    humanUrl: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/depgd/
    baseUrl: https://host:port/management/weblogic/latest/edit/appDeployments
    tags:
      - Applications
      - Deployment
      - DevOps
      - Libraries
      - Resources
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/depgd/
      - type: OpenAPI
        url: openapi/weblogic-deployment-openapi.yml
      - type: JSONSchema
        url: json-schema/weblogic-application-deployment.json
      - type: JSONLD
        url: json-ld/weblogic-context.jsonld
  - name: WebLogic WLST (WebLogic Scripting Tool) API
    description: Python-based scripting interface for automating WebLogic Server administration tasks. Supports online (connected) and offline modes for configuring, deploying, and managing WebLogic domains programmatically.
    humanUrl: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlstc/
    tags:
      - Automation
      - CLI
      - Python
      - Scripting
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlstc/
      - type: Reference
        url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlstg/
  - name: WebLogic JMX API
    description: Java Management Extensions API for programmatic access to WebLogic Server MBeans. Provides the same management capabilities as the REST API via JMX connections, suitable for Java-based management clients and monitoring tools.
    humanUrl: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/jmxcu/
    tags:
      - Java
      - JMX
      - Management
      - MBeans
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/jmxcu/
      - type: API Reference
        url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlmbr/
common:
  - type: Portal
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/
  - type: Getting Started
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/intro/
  - type: Downloads
    url: https://www.oracle.com/middleware/technologies/weblogic-server-downloads.html
  - type: Support
    url: https://support.oracle.com
  - type: Community
    url: https://community.oracle.com/tech/developers/categories/weblogic-server
  - type: Blog
    url: https://blogs.oracle.com/weblogicserver/
  - type: Website
    url: https://www.oracle.com/middleware/technologies/weblogic.html
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms.html
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
  - type: GitHub Organization
    url: https://github.com/oracle
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/weblogic
  - type: YouTube
    url: https://www.youtube.com/@OracleDevelopers
  - type: Status
    url: https://ocistatus.oraclecloud.com/
  - type: Vocabulary
    url: vocabulary/weblogic-vocabulary.yml
  - type: SpectralRules
    url: rules/weblogic-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Application Server
  - Enterprise
  - Java EE
  - Middleware
  - Oracle
  - WebLogic
---
