---
access_model:
  confidence: high
  label: Enterprise · Open access
  onboarding: open
  pricing: enterprise
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 2
  name: Spring Security Agentic Access
  operation_count: 23
  slug: spring-security-agentic-access
  summary_line: 23 operations · 11 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: Core security features for authentication and authorization. Provides UserDetailsService, password encoding, security context management, method security, and HTTP security configuration.
  name: Spring Security Core
  slug: spring-security-core
- description: SAML 2.0 Service Provider support for Spring Security. Enables SSO integration with SAML identity providers, handling authentication requests, assertions, and SLO (Single Logout).
  name: Spring Security SAML2
  slug: spring-security-saml
- description: LDAP authentication and authorization support for Spring Security. Supports LDAP bind authentication, password comparison, and user details loading from directory services.
  name: Spring Security LDAP
  slug: spring-security-ldap
- description: Reactive security for Spring WebFlux applications. Provides non-blocking authentication, authorization, OAuth2 reactive client support, and CSRF protection for reactive web stacks.
  name: Spring Security WebFlux
  slug: spring-security-webflux
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Authorization API from Spring Security — 1 operation(s) for authorization.
  name: Spring Security Authorization API
  slug: spring-security-authorization-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Client Management API from Spring Security — 1 operation(s) for client management.
  name: Spring Security Client Management API
  slug: spring-security-client-management-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Device API from Spring Security — 1 operation(s) for device.
  name: Spring Security Device API
  slug: spring-security-device-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Discovery API from Spring Security — 2 operation(s) for discovery.
  name: Spring Security Discovery API
  slug: spring-security-discovery-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Keys API from Spring Security — 1 operation(s) for keys.
  name: Spring Security Keys API
  slug: spring-security-keys-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The OpenID Connect API from Spring Security — 2 operation(s) for openid connect.
  name: Spring Security OpenID Connect API
  slug: spring-security-openid-connect-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Session API from Spring Security — 2 operation(s) for session.
  name: Spring Security Session API
  slug: spring-security-session-api
- baseURL: http://localhost:8080
  baseurl_source: declared
  description: The Token API from Spring Security — 3 operation(s) for token.
  name: Spring Security Token API
  slug: spring-security-token-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spring Authorization Server API
  slug: open-spring-authorization-server
- collection_type: open
  name: Spring Server Authorization API
  slug: open-spring-security-authorization-api
- collection_type: open
  name: Spring Server Authorization Client Management API
  slug: open-spring-security-client-management-api
- collection_type: open
  name: Spring Server Authorization Device API
  slug: open-spring-security-device-api
- collection_type: open
  name: Spring Server Authorization Discovery API
  slug: open-spring-security-discovery-api
- collection_type: open
  name: Spring Server Authorization Keys API
  slug: open-spring-security-keys-api
- collection_type: open
  name: Spring Security OAuth2 API
  slug: open-spring-security-oauth2
- collection_type: open
  name: Spring Server Authorization OpenID Connect API
  slug: open-spring-security-openid-connect-api
- collection_type: open
  name: Spring Server Authorization Session API
  slug: open-spring-security-session-api
- collection_type: open
  name: Spring Server Authorization Token API
  slug: open-spring-security-token-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/spring-projects/spring-security/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/spring-projects/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/spring-projects/spring-security/blob/main/CONTRIBUTING.adoc
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-security-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spring-security-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog/category/security
- group: operate
  title: ''
  type: Community
  url: https://stackoverflow.com/questions/tagged/spring-security
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SpringSecurity
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/spring-projects/spring-security/issues
- group: docs
  title: ''
  type: Contributing Guide
  url: https://github.com/spring-projects/spring-security/blob/main/CONTRIBUTING.adoc
- group: commercial
  title: ''
  type: License
  url: https://github.com/spring-projects/spring-security/blob/main/LICENSE.txt
- group: other
  title: ''
  type: Maven Repository
  url: https://mvnrepository.com/artifact/org.springframework.security
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/spring-projects/spring-security/releases
created: '2024-01-15'
description: Spring Security is a powerful and highly customizable authentication and access-control framework for Java applications. It is the de-facto standard for securing Spring-based applications, providing comprehensive security services including authentication, authorization, protection against common exploits (CSRF, session fixation, clickjacking), OAuth 2.0, OpenID Connect, SAML 2.0, LDAP, and WebFlux reactive security.
examples:
- key_count: 4
  name: Spring Security Issue Token Example
  slug: spring-security-issue-token-example
finops:
- name: Spring Security Finops
  service_category: Identity
  slug: spring-security-finops
image: https://spring.io/img/projects/spring-security.svg
json_schemas:
- name: Spring Security OAuth2 Token
  property_count: 6
  slug: spring-security-token
json_structures:
- name: Spring Security Token Structure
  property_count: 0
  slug: spring-security-token-structure
jsonld:
- class_count: 5
  name: Spring Security Context
  property_count: 23
  slug: spring-security-context
layout: provider
modified: '2026-05-19'
name: Spring Security
nav: Providers
network: true
overview: 'Spring Security publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Client Management API, Device API, and 5 more. Tagged areas include Authentication, Authorization, Java, JWT, and OpenID Connect.


  The Spring Security catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Security''s developer surface includes authentication, engineering blog, changelog, and 12 more developer resources.'
plans:
- name: Spring Security Plans Pricing
  plan_count: 1
  slug: spring-security-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Spring Security Rate Limits
  slug: spring-security-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spring Security API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spring-security-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Spring Security API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: spring-security-rules
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.5
    catalog_earned_first_party: 0.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 52.9
    developer_ergonomics: 42.9
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-security/refs/heads/main/screenshots/spring-security-2026-06-20T194415.png
security:
- kind: authentication
  name: Spring Security Authentication
  slug: spring-security-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Spring Security Domain Security
  slug: spring-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Security Vulnerability Disclosure
  slug: spring-security-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-security
tags:
- Authentication
- Authorization
- Java
- JWT
- OpenID Connect
- SAML
- Security
- Spring Framework
website: https://spring.io/projects/spring-security
---
