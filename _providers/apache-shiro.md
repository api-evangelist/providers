---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Apache Shiro Agentic Access
  operation_count: 10
  slug: apache-shiro-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 5
apis:
- description: The Authentication API from Apache Shiro — 3 operation(s) for authentication.
  name: Apache Shiro Authentication API
  slug: apache-shiro-authentication-api
- description: The Authorization API from Apache Shiro — 2 operation(s) for authorization.
  name: Apache Shiro Authorization API
  slug: apache-shiro-authorization-api
- description: The Cryptography API from Apache Shiro — 1 operation(s) for cryptography.
  name: Apache Shiro Cryptography API
  slug: apache-shiro-cryptography-api
- description: The Sessions API from Apache Shiro — 1 operation(s) for sessions.
  name: Apache Shiro Sessions API
  slug: apache-shiro-sessions-api
- description: The Users API from Apache Shiro — 1 operation(s) for users.
  name: Apache Shiro Users API
  slug: apache-shiro-users-api
artifact_total: 72
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Shiro REST Authentication API
  slug: open-apache-shiro-authentication-api
- collection_type: open
  name: Apache Shiro REST Authentication Authorization API
  slug: open-apache-shiro-authorization-api
- collection_type: open
  name: Apache Shiro REST Authentication Cryptography API
  slug: open-apache-shiro-cryptography-api
- collection_type: open
  name: Apache Shiro REST Authentication Sessions API
  slug: open-apache-shiro-sessions-api
- collection_type: open
  name: Apache Shiro REST Authentication Users API
  slug: open-apache-shiro-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-shiro-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-shiro-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-shiro-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/shiro
- group: docs
  title: ''
  type: Documentation
  url: https://shiro.apache.org/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-shiro-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-shiro-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-shiro-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://shiro.apache.org/news
created: '2026-03-16'
description: Apache Shiro is a powerful and easy-to-use Java security framework that performs authentication, authorization, cryptography, and session management. It provides a clean API for securing applications from the smallest mobile applications to the largest enterprise systems.
examples:
- key_count: 3
  name: Apache Shiro Hash Request Example
  slug: apache-shiro-hash-request-example
- key_count: 4
  name: Apache Shiro Hash Result Example
  slug: apache-shiro-hash-result-example
- key_count: 3
  name: Apache Shiro Login Request Example
  slug: apache-shiro-login-request-example
- key_count: 4
  name: Apache Shiro Login Response Example
  slug: apache-shiro-login-response-example
- key_count: 1
  name: Apache Shiro Permission Check Request Example
  slug: apache-shiro-permission-check-request-example
- key_count: 3
  name: Apache Shiro Permission Check Result Example
  slug: apache-shiro-permission-check-result-example
- key_count: 2
  name: Apache Shiro Role List Example
  slug: apache-shiro-role-list-example
- key_count: 6
  name: Apache Shiro Session Example
  slug: apache-shiro-session-example
- key_count: 4
  name: Apache Shiro Token Response Example
  slug: apache-shiro-token-response-example
- key_count: 5
  name: Apache Shiro User Example
  slug: apache-shiro-user-example
- key_count: 2
  name: Apache Shiro User List Example
  slug: apache-shiro-user-list-example
- key_count: 4
  name: Apache Shiro User Request Example
  slug: apache-shiro-user-request-example
features:
- description: Pluggable authentication with username/password, remember-me, and token support
  name: Authentication
- description: Role-based and permission-based access control with wildcard permissions
  name: Authorization
- description: Native session management independent of HTTP containers
  name: Session Management
- description: Password hashing with salt, bcrypt, Argon2, and SHA-256
  name: Cryptography
- description: JDBC, LDAP, properties file, and custom realm support
  name: Multiple Realms
- description: Filter-based web application security with URL pattern matching
  name: Web Integration
- description: AOP and annotation-based security for method-level authorization
  name: Annotations
finops:
- name: Apache Shiro Finops
  service_category: API
  slug: apache-shiro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-shiro.png
integrations:
- description: Shiro Spring integration for bean-level security
  name: Spring Framework
- description: Java EE web filter integration for servlet containers
  name: Jakarta EE
- description: LDAP realm for enterprise user directory authentication
  name: LDAP/Active Directory
- description: Database-backed realm for user and permission storage
  name: JDBC
- description: Distributed session management with Hazelcast
  name: Hazelcast
json_schemas:
- name: HashRequest
  property_count: 3
  slug: apache-shiro-hash-request
- name: HashResult
  property_count: 4
  slug: apache-shiro-hash-result
- name: LoginRequest
  property_count: 3
  slug: apache-shiro-login-request
- name: LoginResponse
  property_count: 4
  slug: apache-shiro-login-response
- name: PermissionCheckRequest
  property_count: 1
  slug: apache-shiro-permission-check-request
- name: PermissionCheckResult
  property_count: 3
  slug: apache-shiro-permission-check-result
- name: RoleList
  property_count: 2
  slug: apache-shiro-role-list
- name: Session
  property_count: 6
  slug: apache-shiro-session
- name: TokenResponse
  property_count: 4
  slug: apache-shiro-token-response
- name: UserList
  property_count: 2
  slug: apache-shiro-user-list
- name: UserRequest
  property_count: 4
  slug: apache-shiro-user-request
- name: User
  property_count: 5
  slug: apache-shiro-user
json_structures:
- name: Apache Shiro Hash Request Structure
  property_count: 3
  slug: apache-shiro-hash-request-structure
- name: Apache Shiro Hash Result Structure
  property_count: 4
  slug: apache-shiro-hash-result-structure
- name: Apache Shiro Login Request Structure
  property_count: 3
  slug: apache-shiro-login-request-structure
- name: Apache Shiro Login Response Structure
  property_count: 4
  slug: apache-shiro-login-response-structure
- name: Apache Shiro Permission Check Request Structure
  property_count: 1
  slug: apache-shiro-permission-check-request-structure
- name: Apache Shiro Permission Check Result Structure
  property_count: 3
  slug: apache-shiro-permission-check-result-structure
- name: Apache Shiro Role List Structure
  property_count: 2
  slug: apache-shiro-role-list-structure
- name: Apache Shiro Session Structure
  property_count: 6
  slug: apache-shiro-session-structure
- name: Apache Shiro Token Response Structure
  property_count: 4
  slug: apache-shiro-token-response-structure
- name: Apache Shiro User List Structure
  property_count: 2
  slug: apache-shiro-user-list-structure
- name: Apache Shiro User Request Structure
  property_count: 4
  slug: apache-shiro-user-request-structure
- name: Apache Shiro User Structure
  property_count: 5
  slug: apache-shiro-user-structure
jsonld:
- class_count: 12
  name: Apache Shiro Context
  property_count: 26
  slug: apache-shiro-context
layout: provider
modified: '2026-05-19'
name: Apache Shiro
nav: Providers
network: true
overview: 'Apache Shiro publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Authorization API, Cryptography API, and 2 more. Tagged areas include Authentication, Authorization, Cryptography, Java, and Security.


  The Apache Shiro catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Shiro''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Shiro Plans Pricing
  plan_count: 3
  slug: apache-shiro-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Apache Shiro Rate Limits
  slug: apache-shiro-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Shiro API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-shiro-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Apache Shiro API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 6
  slug: apache-shiro-spectral-rules
score:
  band: thin
  composite: 29.8
  delta: -6.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 53.8
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-shiro/refs/heads/main/screenshots/apache-shiro-2026-06-20T172141.png
security:
- kind: domain-security
  name: Apache Shiro Domain Security
  slug: apache-shiro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Shiro Vulnerability Disclosure
  slug: apache-shiro-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-shiro
tags:
- Authentication
- Authorization
- Cryptography
- Java
- Security
- Apache
- Open Source
use_cases:
- description: Secure Java web applications with authentication and URL-based access control
  name: Web Application Security
- description: Protect REST APIs with token authentication and permission checks
  name: REST API Security
- description: Stateless JWT authentication for microservice architectures
  name: Microservice Auth
- description: Role-based admin interface with fine-grained permissions
  name: Admin Portal Security
---
