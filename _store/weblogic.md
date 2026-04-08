---
aid: weblogic
url: https://raw.githubusercontent.com/api-evangelist/weblogic/refs/heads/main/apis.yml
apis:
- name: WebLogic RESTful Management Services API
  description: RESTful API for monitoring and managing WebLogic Server domains, servers, applications, and resources.
  image: https://www.oracle.com/a/ocom/img/weblogic-server.png
  humanUrl: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/restm/
  baseUrl: https://host:port/management/weblogic/latest
  tags:
  - Configuration
  - Management
  - Monitoring
  - REST
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
  - type: JSONLD
    url: json-ld/weblogic-context.jsonld
  contact:
  - FN: Oracle Support
    url: https://support.oracle.com
- name: WebLogic Monitoring and Diagnostics API
  description: API for accessing runtime monitoring data, metrics, and diagnostics information.
  humanUrl: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/wlrst/
  baseUrl: https://host:port/management/wls/latest
  tags:
  - Diagnostics
  - Metrics
  - Monitoring
  - Performance
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
  description: API for deploying, undeploying, and managing applications and resources.
  humanUrl: https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/depgd/
  baseUrl: https://host:port/management/weblogic/latest/edit/appDeployments
  tags:
  - Applications
  - Deployment
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
  description: Python-based scripting interface for automating WebLogic Server administration tasks.
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
  description: Java Management Extensions API for programmatic access to WebLogic Server MBeans.
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
name: Oracle WebLogic Server APIs
tags:
- Application Server
- Enterprise
- Java EE
- Middleware
- Oracle
- WebLogic
type: Contract
image: https://www.oracle.com/a/ocom/img/weblogic-server.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs and resources for Oracle WebLogic Server administration and management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

