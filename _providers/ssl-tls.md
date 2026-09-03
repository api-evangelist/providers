---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Ssl Tls Agentic Access
  operation_count: 11
  slug: ssl-tls-agentic-access
  summary_line: 11 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: DigiCert provides enterprise certificate management through a REST API supporting issuance, renewal, revocation, and lifecycle management for OV, EV, DV, and private certificates. Supports CT log inte
  name: DigiCert Certificate Management API
  slug: digicert-api
- description: Sectigo (formerly Comodo CA) provides certificate lifecycle management APIs for enterprise PKI, including S/MIME, code signing, and TLS certificates.
  name: Sectigo Certificate Manager API
  slug: sectigo-api
- baseURL: https://acme-v02.api.letsencrypt.org/directory
  baseurl_source: declared
  description: Certificate issuance and management
  name: SSL/TLS Certificates API
  slug: ssl-tls-certificates-api
- baseURL: https://acme-v02.api.letsencrypt.org/directory
  baseurl_source: declared
  description: Domain verification and management
  name: SSL/TLS Domains API
  slug: ssl-tls-domains-api
- baseURL: https://acme-v02.api.letsencrypt.org/directory
  baseurl_source: declared
  description: Certificate expiry monitoring
  name: SSL/TLS Monitoring API
  slug: ssl-tls-monitoring-api
- baseURL: https://acme-v02.api.letsencrypt.org/directory
  baseurl_source: declared
  description: Certificate order lifecycle
  name: SSL/TLS Orders API
  slug: ssl-tls-orders-api
- baseURL: https://acme-v02.api.letsencrypt.org/directory
  baseurl_source: declared
  description: Certificate revocation
  name: SSL/TLS Revocation API
  slug: ssl-tls-revocation-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SSL/TLS Certificate Management API
  slug: open-ssl-tls-certificate-management
- collection_type: open
  name: SSL/TLS Certificate Management Certificates API
  slug: open-ssl-tls-certificates-api
- collection_type: open
  name: SSL/TLS Certificate Management Certificates Domains API
  slug: open-ssl-tls-domains-api
- collection_type: open
  name: SSL/TLS Certificate Management Certificates Monitoring API
  slug: open-ssl-tls-monitoring-api
- collection_type: open
  name: SSL/TLS Certificate Management Certificates Orders API
  slug: open-ssl-tls-orders-api
- collection_type: open
  name: SSL/TLS Certificate Management Certificates Revocation API
  slug: open-ssl-tls-revocation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ssl-tls-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ssl-tls-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ssl-tls-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ssl-tls-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://letsencrypt.org/
- group: docs
  title: ''
  type: Documentation
  url: https://letsencrypt.org/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/letsencrypt
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/openapi/ssl-tls-certificate-management-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/json-schema/ssl-tls-certificate-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/json-structure/ssl-tls-certificate-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/json-ld/ssl-tls-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/rules/ssl-tls-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/vocabulary/ssl-tls-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://letsencrypt.org/feed.xml
created: '2025-01-01'
description: SSL/TLS (Secure Sockets Layer / Transport Layer Security) is the cryptographic protocol that secures communications over the internet. TLS 1.3 is the current standard, providing authentication, confidentiality, and integrity for HTTPS, email, VoIP, and other protocols. This covers certificate management, public key infrastructure (PKI), certificate authorities, and TLS configuration APIs from major vendors and open source projects.
examples:
- key_count: 4
  name: Ssl Tls List Certificates Example
  slug: ssl-tls-list-certificates-example
- key_count: 4
  name: Ssl Tls Request Certificate Example
  slug: ssl-tls-request-certificate-example
finops:
- name: Ssl Tls Finops
  service_category: Identity
  slug: ssl-tls-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ssl-tls.png
json_schemas:
- name: SSL/TLS Certificate
  property_count: 17
  slug: ssl-tls-certificate
json_structures:
- name: Ssl Tls Certificate Structure
  property_count: 0
  slug: ssl-tls-certificate-structure
jsonld:
- class_count: 20
  name: Ssl Tls Context
  property_count: 7
  slug: ssl-tls-context
layout: provider
modified: '2026-05-19'
name: SSL/TLS
nav: Providers
network: true
overview: 'SSL/TLS publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Certificates API, Domains API, Monitoring API, and 2 more. Tagged areas include SSL/TLS, TLS, Certificates, PKI, and Cryptography.


  The SSL/TLS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SSL/TLS''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Ssl Tls Plans Pricing
  plan_count: 1
  slug: ssl-tls-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 7
  name: Ssl Tls Rate Limits
  slug: ssl-tls-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SSL/TLS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ssl-tls-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: SSL/TLS API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: ssl-tls-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 52.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 57.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ssl-tls/refs/heads/main/screenshots/ssl-tls-2026-06-20T194435.png
security:
- kind: authentication
  name: Ssl Tls Authentication
  slug: ssl-tls-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ssl Tls Domain Security
  slug: ssl-tls-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ssl Tls Vulnerability Disclosure
  slug: ssl-tls-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ssl-tls
tags:
- SSL/TLS
- TLS
- Certificates
- PKI
- Cryptography
- Certificate Authority
- HTTPS
website: https://letsencrypt.org/
---
