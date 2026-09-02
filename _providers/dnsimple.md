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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Dnsimple Agentic Access
  operation_count: 18
  slug: dnsimple-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 7
apis:
- description: The Accounts API from DNSimple — 1 operation(s) for accounts.
  name: DNSimple Accounts API
  slug: dnsimple-accounts-api
- description: The Certificates API from DNSimple — 1 operation(s) for certificates.
  name: DNSimple Certificates API
  slug: dnsimple-certificates-api
- description: The Contacts API from DNSimple — 1 operation(s) for contacts.
  name: DNSimple Contacts API
  slug: dnsimple-contacts-api
- description: The Domains API from DNSimple — 2 operation(s) for domains.
  name: DNSimple Domains API
  slug: dnsimple-domains-api
- description: The Webhooks API from DNSimple — 1 operation(s) for webhooks.
  name: DNSimple Webhooks API
  slug: dnsimple-webhooks-api
- description: The Whoami API from DNSimple — 1 operation(s) for whoami.
  name: DNSimple Whoami API
  slug: dnsimple-whoami-api
- description: The Zones API from DNSimple — 4 operation(s) for zones.
  name: DNSimple Zones API
  slug: dnsimple-zones-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DNSimple Accounts API
  slug: open-dnsimple-accounts-api
- collection_type: open
  name: DNSimple Accounts Certificates API
  slug: open-dnsimple-certificates-api
- collection_type: open
  name: DNSimple Accounts Contacts API
  slug: open-dnsimple-contacts-api
- collection_type: open
  name: DNSimple Accounts Domains API
  slug: open-dnsimple-domains-api
- collection_type: open
  name: DNSimple Accounts Webhooks API
  slug: open-dnsimple-webhooks-api
- collection_type: open
  name: DNSimple Accounts Whoami API
  slug: open-dnsimple-whoami-api
- collection_type: open
  name: DNSimple Accounts Zones API
  slug: open-dnsimple-zones-api
- collection_type: open
  name: DNSimple API
  slug: open-dnsimple
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dnsimple-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dnsimple-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dnsimple-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dnsimple-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dnsimple
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dnsimple
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.dnsimple.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.dnsimple.com/feed.xml
created: '2025-02-09'
description: DNSimple is a domain management and DNS hosting service that provides users with a simple and easy way to manage their domain names and DNS settings. With DNSimple, users can register new domain names, transfer existing ones, and easily update DNS records to point their domains to the desired servers. The service also offers features like automatic SSL certificate provisioning, domain forwarding, and email forwarding to help users optimize their online presence.
finops:
- name: Dnsimple Finops
  service_category: API
  slug: dnsimple-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dnsimple.png
layout: provider
modified: '2026-05-19'
name: DNSimple
nav: Providers
network: true
overview: 'DNSimple publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Certificates API, Contacts API, and 4 more. Tagged areas include DNS and Domains.


  DNSimple''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Dnsimple Plans Pricing
  plan_count: 3
  slug: dnsimple-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Dnsimple Rate Limits
  slug: dnsimple-rate-limits
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 14.3
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 25.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dnsimple/refs/heads/main/screenshots/dnsimple-2026-06-20T180100.png
security:
- kind: authentication
  name: Dnsimple Authentication
  slug: dnsimple-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dnsimple Domain Security
  slug: dnsimple-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dnsimple
tags:
- DNS
- Domains
---
