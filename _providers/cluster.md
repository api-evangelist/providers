---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cluster/refs/heads/main/llms/cluster-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cluster-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cluster/refs/heads/main/hosts/cluster-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cluster-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cluster/refs/heads/main/vendors/cluster-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cluster-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datacluster.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cluster/refs/heads/main/security/cluster-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cluster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datacluster.com
coverage:
  checked: '2026-10-09'
  detail: Docs at https://docs.datacluster.com/ render a Stoplight page with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.datacluster.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cluster provides a product data API and eCommerce intelligence platform, building the data infrastructure that powers AI-driven commerce. It offers comprehensive product information, pricing, availability, and rich attributes to help businesses enhance their online catalogs and analytics.
image: https://storage.googleapis.com/gpt-engineer-file-uploads/attachments/og-images/35443dfd-5a5b-45e3-b5c6-99a497a2d290?Expires=1775462303&GoogleAccessId=go-api-on-aws%40gpt-engineer-390607.iam.gserviceaccount.com&Signature=sj4mO3YH3zgj18BtNqmdtiUqdJUk2R%2Fpas08eT4ZN4npEZipin%2F%2B319tH%2BlT7eYGTZCggA618TI%2FZnBclE8I9LeyGWof3C%2BSg%2FvOdXR31IqniXyKktg1En%2Fn57a3RZ8wNG2IzhvldPK%2FmWVr1p7xG9aon7ONIPgzZP5rqC6oUdwpiozhT0eWvaRwF93S16xsqSwcv9CSNUz6vGr%2BBvQ2ZGMPmwbD42ILKczgLNPZRgfKgJ020aLh7TzIOcv%2B7cq0oHcoqXE%2FpU30BH%2B1bYPPv33Pzz2TasGdmJEIIeVbEDSScKJWz5XVsWi%2BxLNyfHm%2F14eFKWMQmXvFw3ByuzZIkQ%3D%3D
layout: provider
modified: '2026-10-09'
name: Cluster
nav: Providers
network: true
overview: 'Cluster is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, E-Commerce, and Product.


  Cluster''s developer surface includes documentation and 5 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cluster Domain Security
  slug: cluster-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cluster
tags:
- Company
- Data
- E-Commerce
- Product
website: https://datacluster.com
---
