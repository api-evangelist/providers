---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-10-17'
api_count: 3
apis:
- baseURL: https://api.cloudsmith.io
  baseurl_source: declared
  description: The Metadata API from Cloudsmithio — 1 operation(s) for metadata.
  name: Cloudsmithio Metadata API
  slug: cloudsmithio-metadata-api
- baseURL: https://api.cloudsmith.io
  baseurl_source: declared
  description: The Package API from Cloudsmithio — 1 operation(s) for package.
  name: Cloudsmithio Package API
  slug: cloudsmithio-package-api
- baseURL: https://api.cloudsmith.io
  baseurl_source: declared
  description: The User API from Cloudsmithio — 2 operation(s) for user.
  name: Cloudsmithio User API
  slug: cloudsmithio-user-api
artifact_total: 12
asyncapis:
- description: ''
  name: Cloudsmithio Webhooks
  slug: cloudsmithio-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/rate-limits/cloudsmithio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudsmithio-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/rules/cloudsmithio-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudsmithio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/json-ld/cloudsmithio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudsmithio-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/vocabulary/cloudsmithio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudsmithio-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/asyncapi/cloudsmithio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cloudsmithio-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/data-model/cloudsmithio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudsmithio-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/authentication/cloudsmithio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudsmithio-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/conformance/cloudsmithio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudsmithio-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/llms/cloudsmithio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudsmithio-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/well-known/cloudsmithio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudsmithio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/hosts/cloudsmithio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudsmithio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/vendors/cloudsmithio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudsmithio-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://cloudsmith.com/product/integrations/webhooks
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cloudsmith.com
- group: operate
  title: ''
  type: Support
  url: https://support.cloudsmith.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudsmith.com
- group: auth
  title: ''
  type: Security
  url: https://cloudsmith.com/blog/category/security/page/1
- group: company
  title: ''
  type: Newsroom
  url: https://cloudsmith.com/company/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudsmith-io
- group: operate
  title: ''
  type: ChangeLog
  url: https://cloudsmith.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://cloudsmith.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudsmith.com/authentication/setup-cloudsmith-to-authenticate-with-oidc-in-github-actions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudsmith.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudsmithio/refs/heads/main/security/cloudsmithio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudsmithio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudsmith.com
coverage:
  checked: '2026-10-09'
  detail: API documentation pages return JavaScript-rendered shells with no machine‑readable spec.
  evidence:
  - status: 302
    url: https://cloudsmith.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cloudsmith is a fully-managed artifact management, software supply chain security, and software distribution platform. It provides secure, scalable, developer‑friendly solutions for managing packages, containers, and ML models, with features like vulnerability scanning, policy enforcement, and detailed observability. The service supports a wide range of formats and integrates with CI/CD pipelines, helping organizations protect their software supply chain from attacks and compliance issues.
image: https://cloudsmith.com/images/opengraph.png
json_schemas:
- name: GetUserSelfResponse
  property_count: 1
  slug: cloudsmithio-get-user-self-response
- name: PostMetadataValidateRequest
  property_count: 2
  slug: cloudsmithio-post-metadata-validate-request
- name: PostMetadataValidateResponse
  property_count: 3
  slug: cloudsmithio-post-metadata-validate-response
jsonld:
- class_count: 3
  name: Cloudsmithio Context
  property_count: 3
  slug: cloudsmithio-context
layout: provider
modified: '2026-10-09'
name: Cloudsmithio
nav: Providers
network: true
overview: 'Cloudsmithio is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Metadata API, Package API, and User API. Tagged areas include Artifact Management, Software Supply Chain, Security, DevOps, and Cloud.


  The Cloudsmithio catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cloudsmithio''s developer surface includes authentication, support, changelog, engineering blog, getting-started guide, documentation, and 19 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 6
  name: Cloudsmithio Rate Limits
  slug: cloudsmithio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Cloudsmithio API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: cloudsmithio-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 22.0
    contract_quality: 29.3
    developer_ergonomics: 40.5
    discoverability: 80.4
    operational_transparency: 86.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Cloudsmithio Authentication
  slug: cloudsmithio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cloudsmithio Domain Security
  slug: cloudsmithio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudsmithio
tags:
- Artifact Management
- Software Supply Chain
- Security
- DevOps
- Cloud
website: https://cloudsmith.com
---
