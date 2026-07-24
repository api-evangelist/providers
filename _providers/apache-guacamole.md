---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Apache Guacamole Agentic Access
  operation_count: 14
  slug: apache-guacamole-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 7
apis:
- description: JavaScript client library for embedding the Guacamole remote desktop client in web applications, with APIs for protocol tunneling, display rendering, and user input handling.
  name: Apache Guacamole JavaScript Client API
  slug: apache-guacamole-javascript-api
- description: Active connection session management
  name: Apache Guacamole Active Connections API
  slug: apache-guacamole-active-connections-api
- description: Authentication token management
  name: Apache Guacamole Authentication API
  slug: apache-guacamole-authentication-api
- description: Remote desktop connection management
  name: Apache Guacamole Connections API
  slug: apache-guacamole-connections-api
- description: Connection history and audit logs
  name: Apache Guacamole History API
  slug: apache-guacamole-history-api
- description: User group management
  name: Apache Guacamole User Groups API
  slug: apache-guacamole-user-groups-api
- description: User account management
  name: Apache Guacamole Users API
  slug: apache-guacamole-users-api
artifact_total: 57
collections:
- collection_type: open
  name: Apache Guacamole REST API
  slug: open-apache-guacamole-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-guacamole-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-guacamole-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-guacamole-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-guacamole-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://guacamole.apache.org/doc/gug/
- group: start
  title: ''
  type: GettingStarted
  url: https://guacamole.apache.org/doc/gug/users-guide.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/guacamole-client
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-guacamole-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-guacamole-vocabulary.yaml
created: '2026-03-16'
description: Apache Guacamole is a clientless remote desktop gateway that supports standard protocols like VNC, RDP, and SSH. It requires no plugins or client software and provides access to remote desktops through a web browser with a comprehensive REST API for connection, user, and session management.
examples:
- key_count: 5
  name: Guacamole Rest Active Connection Example
  slug: guacamole-rest-active-connection-example
- key_count: 4
  name: Guacamole Rest Auth Token Example
  slug: guacamole-rest-auth-token-example
- key_count: 6
  name: Guacamole Rest Connection Example
  slug: guacamole-rest-connection-example
- key_count: 5
  name: Guacamole Rest Connection Group Example
  slug: guacamole-rest-connection-group-example
- key_count: 6
  name: Guacamole Rest Connection History Entry Example
  slug: guacamole-rest-connection-history-entry-example
- key_count: 4
  name: Guacamole Rest User Example
  slug: guacamole-rest-user-example
- key_count: 2
  name: Guacamole Rest User Group Example
  slug: guacamole-rest-user-group-example
features:
- description: Access remote desktops through any HTML5 web browser with no client software or plugins required.
  name: Clientless Remote Desktop
- description: Supports VNC, RDP, SSH, and Telnet protocols through a unified web gateway.
  name: Multi-Protocol Support
- description: Stateless REST API authentication using time-limited tokens from the /api/tokens endpoint.
  name: Token-Based Authentication
- description: REST API for creating, updating, and organizing remote desktop connections and connection groups.
  name: Connection Management
- description: Fine-grained user and group permissions for controlling access to connections and administrative functions.
  name: User and Group Management
- description: Monitor and terminate active remote desktop sessions through the REST API.
  name: Active Session Monitoring
- description: Audit log of all remote desktop sessions with timestamps and user attribution.
  name: Connection History
- description: Java extension API for implementing custom authentication providers, event listeners, and protocol extensions.
  name: Extension API
finops:
- name: Apache Guacamole Finops
  service_category: API
  slug: apache-guacamole-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-guacamole.png
integrations:
- description: Runs as a Java web application on Apache Tomcat or any Java Servlet container.
  name: Apache Tomcat
- description: LDAP extension for authenticating users against directory services like Active Directory.
  name: LDAP / Active Directory
- description: Multi-factor authentication extensions supporting TOTP apps and Duo Security.
  name: TOTP / Duo MFA
- description: Database authentication extensions for storing connections and users in relational databases.
  name: MySQL / PostgreSQL
- description: Guacamole can be deployed on Kubernetes with the guacamole-client Docker image.
  name: Kubernetes
json_schemas:
- name: ActiveConnection
  property_count: 5
  slug: guacamole-rest-active-connection
- name: AuthToken
  property_count: 4
  slug: guacamole-rest-auth-token
- name: ConnectionGroup
  property_count: 5
  slug: guacamole-rest-connection-group
- name: ConnectionHistoryEntry
  property_count: 6
  slug: guacamole-rest-connection-history-entry
- name: Connection
  property_count: 6
  slug: guacamole-rest-connection
- name: UserGroup
  property_count: 2
  slug: guacamole-rest-user-group
- name: User
  property_count: 4
  slug: guacamole-rest-user
json_structures:
- name: Guacamole Rest Active Connection Structure
  property_count: 5
  slug: guacamole-rest-active-connection-structure
- name: Guacamole Rest Auth Token Structure
  property_count: 4
  slug: guacamole-rest-auth-token-structure
- name: Guacamole Rest Connection Group Structure
  property_count: 5
  slug: guacamole-rest-connection-group-structure
- name: Guacamole Rest Connection History Entry Structure
  property_count: 6
  slug: guacamole-rest-connection-history-entry-structure
- name: Guacamole Rest Connection Structure
  property_count: 6
  slug: guacamole-rest-connection-structure
- name: Guacamole Rest User Group Structure
  property_count: 2
  slug: guacamole-rest-user-group-structure
- name: Guacamole Rest User Structure
  property_count: 4
  slug: guacamole-rest-user-structure
jsonld:
- class_count: 9
  name: Apache Guacamole Rest Context
  property_count: 17
  slug: apache-guacamole-rest-context
layout: provider
modified: '2026-05-19'
name: Apache Guacamole
nav: Providers
network: true
overview: 'Apache Guacamole publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Active Connections API, Authentication API, Connections API, and 3 more. Tagged areas include Apache, Open Source, RDP, Remote Access, and Remote Desktop.


  The Apache Guacamole catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Guacamole''s developer surface includes authentication, documentation, getting-started guide, and 7 more developer resources.'
plans:
- name: Apache Guacamole Plans Pricing
  plan_count: 3
  slug: apache-guacamole-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Apache Guacamole Rate Limits
  slug: apache-guacamole-rate-limits
rules:
- name: Apache Guacamole API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-guacamole-jsonschema-spectral-rules
- name: Apache Guacamole API Rules
  rule_count: 16
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 10
  slug: apache-guacamole-spectral-rules
score:
  band: developing
  composite: 51.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.0
    developer_ergonomics: 30.4
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 51.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-guacamole/refs/heads/main/screenshots/apache-guacamole-2026-06-20T172106.png
security:
- kind: authentication
  name: Apache Guacamole Authentication
  slug: apache-guacamole-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apache Guacamole Domain Security
  slug: apache-guacamole-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Guacamole Vulnerability Disclosure
  slug: apache-guacamole-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-guacamole
tags:
- Apache
- Open Source
- RDP
- Remote Access
- Remote Desktop
- SSH
- VNC
- Web Gateway
use_cases:
- description: Provide browser-based access to Linux and Windows desktops for remote workers.
  name: Remote Desktop Access
- description: Access cloud VMs and servers through SSH and RDP via browser without installing VPN or client software.
  name: Cloud Server Management
- description: Use Guacamole as a protocol-proxying bastion host to isolate internal systems from direct network access.
  name: Secure Bastion Host
- description: Provide developers with browser-based access to containerized or virtualized development environments.
  name: Development Environment Access
- description: Enable IT helpdesk teams to access and troubleshoot user desktops through the browser.
  name: IT Support Tooling
---
