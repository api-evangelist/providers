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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-11'
api_count: 5
apis:
- description: RESTful management API for JBoss Enterprise Application Platform (EAP) administration and monitoring of server configuration, deployments, and runtime state.
  name: JBoss EAP Management API
  slug: jboss-eap-management-api
- description: RESTful interface for WildFly (the community version of JBoss EAP) server management, deployments, and runtime configuration.
  name: WildFly REST API
  slug: wildfly-rest-api
- description: REST API for distributed in-memory caching with JBoss Data Grid (Red Hat Data Grid), based on the Infinispan project.
  name: JBoss Data Grid REST API
  slug: jboss-data-grid-rest-api
- description: Administration REST API for Keycloak identity and access management, supporting OAuth2, OpenID Connect, and SAML for SSO scenarios.
  name: Keycloak Admin REST API
  slug: keycloak-admin-rest-api
- description: REST DSL for Apache Camel integration in JBoss Fuse, enabling definition of REST endpoints and routes for enterprise integration patterns.
  name: JBoss Fuse REST DSL
  slug: jboss-fuse-rest-dsl
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jboss-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jboss-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.redhat.com/products/eap/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jboss.org/get-started/
- group: company
  title: ''
  type: Blog
  url: https://www.jboss.org/posts/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jbossas
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support/
created: '2024-01-15'
description: JBoss is a division of Red Hat providing open source middleware and application server technologies for enterprise Java workloads. The JBoss product portfolio includes JBoss EAP (Enterprise Application Platform), the WildFly community application server, JBoss Data Grid (Red Hat Data Grid), Keycloak identity and access management, and JBoss Fuse integration platform built on Apache Camel. These projects power Jakarta EE deployments, single sign-on, distributed caching, and microservices integration in enterprise environments.
finops:
- name: Jboss Finops
  service_category: API
  slug: jboss-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jboss.png
layout: provider
modified: '2026-04-28'
name: JBoss
nav: Providers
network: true
overview: 'JBoss publishes 2 APIs on the [APIs.io](https://apis.io/) network: EAP Management API and Keycloak Admin REST API. Tagged areas include Application Server, Cloud Native, Enterprise, Jakarta EE, and Java EE.


  JBoss'' developer surface includes developer portal, getting-started guide, engineering blog, support, and 3 more developer resources.'
plans:
- name: Jboss Plans Pricing
  plan_count: 3
  slug: jboss-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 5
  name: Jboss Rate Limits
  slug: jboss-rate-limits
score:
  band: emerging
  composite: 24.7
  delta: -7.8
  facets:
    commercial_clarity: 15.8
    contract_quality: 32.3
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 32.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/jboss/refs/heads/main/screenshots/jboss-2026-06-20T183710.png
security:
- kind: domain-security
  name: Jboss Domain Security
  slug: jboss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jboss Vulnerability Disclosure
  slug: jboss-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jboss
tags:
- Application Server
- Cloud Native
- Enterprise
- Jakarta EE
- Java EE
- Microservices
- Middleware
- Open Source
- Red Hat
website: https://developers.redhat.com/products/eap/overview
---
