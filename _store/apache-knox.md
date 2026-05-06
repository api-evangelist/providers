---
aid: apache-knox
name: Apache Knox
description: Apache Knox is a REST API and application gateway for the Apache Hadoop ecosystem. It provides a single access point for all REST and HTTP interactions with Apache Hadoop clusters, with authentication, authorization, SSO, and audit capabilities. Governed by the Apache Software Foundation under Apache 2.0.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - Authentication
  - Hadoop
  - Open Source
  - Security
  - SSO
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-knox/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-knox:admin-api
    name: Apache Knox Admin REST API
    description: The Knox Admin REST API provides endpoints for topology management, service descriptor management, provider configuration, and version information for administering the Knox gateway.
    humanURL: https://knox.apache.org/books/knox-2-0-0/user-guide.html
    tags:
      - Administration
      - API Gateway
      - REST
    properties:
      - type: Documentation
        url: https://knox.apache.org/books/knox-2-0-0/user-guide.html
      - type: OpenAPI
        url: openapi/apache-knox-admin-api.yaml
  - aid: apache-knox:gateway-api
    name: Apache Knox Gateway API
    description: The Knox gateway proxies and secures access to Hadoop ecosystem services including HDFS WebHDFS, Hive, HBase REST, YARN, Oozie, Ambari, and Ranger with authentication and authorization enforcement.
    humanURL: https://knox.apache.org/books/knox-2-0-0/user-guide.html#Service+Details
    tags:
      - API Gateway
      - Hadoop
      - Proxy
      - Security
    properties:
      - type: Documentation
        url: https://knox.apache.org/books/knox-2-0-0/user-guide.html#Service+Details
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/knox
  - type: Documentation
    url: https://knox.apache.org/books/knox-2-0-0/user-guide.html
  - type: GettingStarted
    url: https://knox.apache.org/books/knox-2-0-0/user-guide.html#Quick+Start
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Versioning
    url: https://knox.apache.org/books/
  - type: SpectralRules
    url: rules/apache-knox-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-knox-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/gateway-management.yaml
  - type: Features
    data:
      - name: Single Access Point
        description: Unified gateway for all Hadoop REST services eliminating direct cluster access.
      - name: Authentication
        description: Kerberos, LDAP, OAuth2, and JWT authentication support.
      - name: SSO Integration
        description: SAML2-based SSO and token-based federation across Hadoop services.
      - name: Authorization
        description: Fine-grained authorization via Apache Ranger integration.
      - name: SSL/TLS Termination
        description: SSL/TLS termination at the gateway for encrypted communication.
      - name: Service Discovery
        description: Automatic service discovery via Ambari and Cloudera Manager integration.
      - name: Topology Management
        description: Dynamic topology configuration without gateway restarts.
      - name: Audit Logging
        description: Comprehensive audit logs for all gateway interactions.
  - type: UseCases
    data:
      - name: Hadoop Cluster Security
        description: Secure and centralize access to all Hadoop REST APIs through Knox.
      - name: Cloud Hadoop Access
        description: Provide secure REST access to EMR, HDInsight, and Dataproc clusters.
      - name: Hadoop SSO
        description: Enable single sign-on across Ambari, Hue, Spark UI, and other Hadoop UIs.
      - name: REST API Proxying
        description: Proxy WebHDFS, Hive JDBC/REST, HBase REST, and YARN REST through Knox.
  - type: Integrations
    data:
      - name: Apache Hadoop HDFS
        description: WebHDFS REST API proxied and secured through Knox.
      - name: Apache Hive
        description: Hive JDBC and REST API access via Knox gateway.
      - name: Apache HBase
        description: HBase REST API proxied through Knox with authentication.
      - name: Apache Ranger
        description: Authorization policy enforcement via Ranger Knox plugin.
      - name: Apache Ambari
        description: Ambari REST API proxied through Knox for cluster management.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
