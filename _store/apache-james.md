---
aid: apache-james
name: Apache James
description: Apache James (Java Apache Mail Enterprise Server) is a portable and enterprise-ready mail server built entirely in Java. It implements SMTP, IMAP, POP3, and JMAP protocols and provides a modular architecture with a comprehensive administration REST API and Cassandra-backed distributed deployment.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Email
  - IMAP
  - Java
  - JMAP
  - Mail Server
  - Open Source
  - SMTP
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-james/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-james:webadmin-rest-api
    name: Apache James WebAdmin REST API
    description: The James WebAdmin API provides REST endpoints for managing domains, users, mailboxes, mail repositories, mail queues, quotas, drop lists, and async tasks. It is the primary management interface for James server instances.
    humanURL: https://james.apache.org/server/manage-webadmin.html
    tags:
      - Administration
      - Email
      - REST
    properties:
      - type: Documentation
        url: https://james.apache.org/server/manage-webadmin.html
      - type: OpenAPI
        url: openapi/apache-james-webadmin-rest-api.yaml
  - aid: apache-james:jmap-api
    name: Apache James JMAP API
    description: The JMAP (JSON Meta Application Protocol) implementation in James provides a modern, efficient email protocol for synchronizing messages, mailboxes, contacts, and calendars for email clients.
    humanURL: https://james.apache.org/server/rfcs-compliance.html
    tags:
      - Email
      - JMAP
      - JSON
    properties:
      - type: Documentation
        url: https://james.apache.org/server/rfcs-compliance.html
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/james-project
  - type: Documentation
    url: https://james.apache.org/documentation.html
  - type: GettingStarted
    url: https://james.apache.org/server/quick-start.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Blog
    url: https://james.apache.org/blog/
  - type: Versioning
    url: https://james.apache.org/download.cgi
  - type: SpectralRules
    url: rules/apache-james-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-james-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/mail-server-management.yaml
  - type: Features
    data:
      - name: SMTP Server
        description: Full SMTP server implementation with TLS, DKIM, SPF, and DMARC support.
      - name: IMAP Server
        description: IMAP4 server with full RFC compliance for email client access.
      - name: JMAP Support
        description: Modern JMAP protocol implementation for efficient email synchronization.
      - name: WebAdmin REST API
        description: HTTP REST API for complete server administration without downtime.
      - name: Distributed Architecture
        description: Cassandra-backed distributed deployment for high availability.
      - name: Modular Design
        description: Pluggable architecture supporting custom protocols, storage, and authentication.
      - name: Mail Queuing
        description: Persistent mail queuing with configurable retry strategies.
      - name: Quota Management
        description: Per-user, per-domain, and global mailbox and message quota enforcement.
  - type: UseCases
    data:
      - name: Enterprise Mail Server
        description: Deploy a full-featured enterprise mail server with SMTP, IMAP, and JMAP.
      - name: Mail Server Migration
        description: Migrate from other mail servers with full protocol compatibility.
      - name: Automated Email Processing
        description: Build automated email pipelines using James mailet and matcher APIs.
      - name: High-Availability Mail
        description: Deploy distributed James clusters with Cassandra and RabbitMQ for HA.
  - type: Integrations
    data:
      - name: Apache Cassandra
        description: Distributed mail storage backend for high availability deployments.
      - name: Apache Kafka
        description: Event bus integration for distributed James deployments.
      - name: RabbitMQ
        description: AMQP message queue for inter-node communication.
      - name: Elasticsearch/OpenSearch
        description: Full-text mail search indexing via Elasticsearch integration.
      - name: OpenLDAP
        description: LDAP authentication and directory integration for user management.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
