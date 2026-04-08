---
aid: oracle-weblogic
url: https://raw.githubusercontent.com/api-evangelist/oracle-weblogic/refs/heads/main/apis.yml
apis:
- name: WebLogic RESTful Management Services API
  description: RESTful API for managing and monitoring WebLogic Server domains, servers, applications, and resources.
  image: https://www.oracle.com/a/ocom/img/weblogic-server.png
  humanURL: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlrest/index.html
  baseURL: http://localhost:7001/management/weblogic/latest
  tags:
  - Management
  - Monitoring
  - REST
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlrest/index.html
  - type: OpenAPI
    url: openapi/oracle-weblogic-management-openapi.yml
  - type: Authentication
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlrest/authentication.html
  - type: JSONSchema
    url: json-schema/oracle-weblogic-server-configuration.json
  - type: JSONSchema
    url: json-schema/oracle-weblogic-data-source.json
  - type: JSONSchema
    url: json-schema/oracle-weblogic-jms-configuration.json
  - type: JSON-LD
    url: json-ld/oracle-weblogic-context.jsonld
- name: WebLogic Monitoring and Diagnostics API
  description: API for accessing runtime monitoring data, diagnostics information, and performance metrics.
  humanURL: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/jmxcu/index.html
  baseURL: http://localhost:7001/management/weblogic/latest/domainRuntime
  tags:
  - Diagnostics
  - JMX
  - Metrics
  - Monitoring
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/jmxcu/index.html
  - type: Guide
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlach/monitor.html
  - type: OpenAPI
    url: openapi/oracle-weblogic-monitoring-openapi.yml
  - type: JSONSchema
    url: json-schema/oracle-weblogic-domain-runtime.json
- name: WebLogic Deployment API
  description: API for deploying, undeploying, and managing application deployments on WebLogic Server.
  humanURL: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlrest/op-management-weblogic-latest-edit-appdeployments-post.html
  baseURL: http://localhost:7001/management/weblogic/latest/edit/appDeployments
  tags:
  - Applications
  - Deployment
  - Lifecycle
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlrest/resources.html
  - type: Tutorial
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/depgd/index.html
  - type: OpenAPI
    url: openapi/oracle-weblogic-deployment-openapi.yml
  - type: JSONSchema
    url: json-schema/oracle-weblogic-deployment.json
- name: WebLogic WLST (WebLogic Scripting Tool) API
  description: Python-based scripting interface for automating WebLogic Server administration tasks.
  humanURL: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlstc/index.html
  baseURL: https://localhost:5556
  tags:
  - Administration
  - Automation
  - Python
  - Scripting
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlstc/index.html
  - type: Reference
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlstg/index.html
- name: WebLogic JMX API
  description: Java Management Extensions API for programmatic management and monitoring of WebLogic Server.
  humanURL: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/jmxcu/index.html
  baseURL: service:jmx:rmi:///jndi/rmi://localhost:7001/jmxrmi
  tags:
  - Java
  - JMX
  - Management
  - MBeans
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/jmxcu/index.html
  - type: API Reference
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlapi/index.html
  - type: Examples
    url: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/jmxcu/examples.html
name: Oracle WebLogic Server
tags:
- Application Server
- Enterprise
- Java EE
- Middleware
- Oracle
type: Contract
image: https://www.oracle.com/a/ocom/img/weblogic-server.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for managing and monitoring Oracle WebLogic Server - a leading platform for building and deploying enterprise Java applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

