---
access_model:
  confidence: high
  label: Free · No signup, no developer portal
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-02'
api_count: 4
apis:
- baseURL: https://sso.ukm.my/saml2/idp
  baseurl_source: declared
  description: 'Universiti Kebangsaan Malaysia''s own SAML 2.0 identity provider, a SimpleSAMLphp deployment at sso.ukm.my. Publishes unauthenticated SAML 2.0 metadata (application/samlmetadata+xml, 4,261 bytes) with '
  name: SSO@UKM — SAML 2.0 Identity Provider
  slug: identity-federation
- baseURL: https://ptsldigital.ukm.my/oai/request
  baseurl_source: declared
  description: DSpace 6.3 institutional repository operated by Perpustakaan Tun Seri Lanang (UKM Library) on the university's own host, holding theses, past-year examination papers and selected government and law pu
  name: UKM Learning and Research Repository (OAI-PMH)
  slug: learning-research-repository-oai
- baseURL: https://ejournal.ukm.my/index.php/index/oai
  baseurl_source: declared
  description: 'Open Journal Systems 2.4.8.1 platform self-hosted at ejournal.ukm.my (CNAME ejournals.ukm.my), carrying the journals published by UKM faculties, institutes and UKM Press. Its OAI-PMH 2.0 interface is '
  name: UKM e-Journal System (OAI-PMH)
  slug: ejournal-oai
- baseURL: https://www.ukm.my/portal/wp-json
  baseurl_source: declared
  description: 'UKM runs its web estate on self-hosted WordPress and leaves the wp/v2 REST API open for unauthenticated reads on its own domain. Two installations were verified live: the main portal at www.ukm.my/por'
  name: UKM Web Content REST API (WordPress wp/v2)
  slug: web-content-rest
- description: EPrints repository of journal articles published by UKM faculties, institutes and UKM Press, registered in OpenDOAR (record 2122) and ROAR as supporting OAI-PMH 2.0 via its EPrints oai2 interface. The
  name: UKM Journal Article Repository (OAI-PMH) — unreachable
  slug: journal-article-repository-oai
- description: 'Three Crossref memberships are held by units of Universiti Kebangsaan Malaysia, together accounting for 16,447 registered DOIs: member 7332, Penerbit Universiti Kebangsaan Malaysia (UKM Press), prefix'
  name: Crossref DOI Registration (UKM Press and UKM faculties)
  slug: crossref-membership
- description: Universiti Kebangsaan Malaysia is registered in the Research Organization Registry as https://ror.org/00bw8d226, created 2018-11-14 and last modified 2026-07-20. The record declares both of the instit
  name: ROR Organization Registration
  slug: ror-registration
- description: Perpustakaan Tun Seri Lanang runs its research and subject guides on a Springshare LibGuides tenant at ukm.libguides.com — an institution-specific subdomain on a vendor platform. The guides, the conte
  name: Springshare LibGuides (tenant deployment)
  slug: libguides-tenant
- description: UKM Library's off-campus access to licensed e-resources runs on a RemoteXs tenant at eresourcesptsl.ukm.remotexs.co — a vendor host carrying a UKM-specific account. The entitlement and the user popula
  name: RemoteXs E-Resources Proxy (tenant deployment)
  slug: remotexs-tenant
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.ukm.my/portal/
- group: company
  title: ''
  type: Blog
  url: https://www.ukm.my/beritaukm/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ukm.my/beritaukm/feed/
- group: docs
  title: ''
  type: APIReference
  url: https://www.ukm.my/portal/wp-json/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sso.ukm.my/saml2/idp/metadata.php
- group: other
  title: ''
  type: ResearchRepository
  url: https://ptsldigital.ukm.my/
- group: other
  title: ''
  type: ResearchRepository
  url: https://ejournal.ukm.my/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.ukm.my/ptsl/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universitikebangsaanmalaysia/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ukm-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ukm-conformance.yml
- group: design
  title: ''
  type: Errors
  url: errors/ukm-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ukm-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ukm-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ukm-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ukm-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ukm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ukm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ukm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Kebangsaan Malaysia (UKM), The National University of Malaysia, is a public research university in Bangi, Selangor, established 1970, ROR https://ror.org/00bw8d226. It publishes no developer portal, no API documentation, no OpenAPI, no changelog, no status page, no robots.txt, no sitemap.xml and no llms.txt — every one of those returns 404 on www.ukm.my. What it does operate, on its own domain and its own infrastructure, is four unauthenticated machine-readable surfaces that it has never described anywhere. The largest is its own identity provider: SSO@UKM at sso.ukm.my is a SimpleSAMLphp SAML 2.0 IdP publishing unauthenticated metadata with signing and encryption keys, SSO and SLO bindings and a technical contact, and it is demonstrably in production — the library''s LibQuest service hands an unauthenticated visitor straight to it as SAML SP smuSSO-sp. UKM is nevertheless absent from eduGAIN; a scan of all 10,615 eduGAIN entities on 2026-09-01 found no ukm.my entity
  while sixteen other Malaysian institutions are registered through SIFULAN. The scholarly surfaces are two live OAI-PMH 2.0 endpoints run by Perpustakaan Tun Seri Lanang (the UKM Library): the DSpace 6.3 UKM Learning and Research Repository at ptsldigital.ukm.my with twelve metadata formats, and the OJS 2.4.8.1 UKM e-Journal System at ejournal.ukm.my with five formats and 100 sets — the latter never previously catalogued here. Both platforms are years past end of support. Behind them sits a real identifier footprint: three Crossref memberships owned by UKM units, led by UKM Press with prefix 10.17576 and 16,243 DOIs. A third repository, journalarticle.ukm.my, is registered in OpenDOAR and ROAR but has not answered on port 80 or 443 across probes in June and September 2026. The fourth surface is incidental rather than intentional: UKM runs its web estate on self-hosted WordPress and leaves the wp/v2 REST API open for unauthenticated reads — 314 routes on the main portal, a second installation
  on the Berita UKM news site. It is the closest thing the university has to a public read API for its own content, and nothing about it is documented or governed. Nothing in this profile is a vendor contract attributed to UKM. Two vendor tenancies are recorded as relationships only — Springshare LibGuides and a RemoteXs e-resources proxy. No course catalog, open data portal, research computing or library discovery API was found; the GEMILANG discovery service did not answer.'
examples:
- key_count: 11
  name: Ukm Portal Wp Json Root
  slug: ukm-portal-wp-json-root
finops:
- name: Ukm Finops
  service_category: Education
  slug: ukm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ukm.png
json_schemas:
- name: UKM Web Content — WordPress page record
  property_count: 23
  slug: ukm-wordpress-page
jsonld:
- class_count: 20
  name: Ukm Context
  property_count: 0
  slug: ukm-context
layout: provider
modified: '2026-09-01'
name: Universiti Kebangsaan Malaysia
nav: Providers
network: true
overview: 'Universiti Kebangsaan Malaysia publishes 4 APIs on the [APIs.io](https://apis.io/) network, including SSO@UKM — SAML 2.0 Identity Provider, UKM Learning and Research Repository (OAI-PMH), UKM e-Journal System (OAI-PMH), and 1 more. Tagged areas include University, Higher Education, Education, Research, and Malaysia.


  The Universiti Kebangsaan Malaysia catalog on APIs.io includes 1 JSON-LD context.


  Universiti Kebangsaan Malaysia''s developer surface includes engineering blog, API reference, authentication, and 17 more developer resources.'
plans:
- name: Ukm Plans Pricing
  plan_count: 2
  slug: ukm-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Ukm Rate Limits
  slug: ukm-rate-limits
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 37.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 15.2
    contract_quality: 62.5
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 15.2
    operational_transparency: 21.1
  previous_composite: 40.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ukm/refs/heads/main/screenshots/ukm-2026-06-20T200011.png
security:
- kind: authentication
  name: Ukm Authentication
  slug: ukm-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ukm Domain Security
  slug: ukm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ukm
tags:
- University
- Higher Education
- Education
- Research
- Malaysia
- Southeast Asia
- Identity Federation
- SAML
- Research Repository
- Institutional Repository
- OAI-PMH
- Open Access
- Scholarly Publishing
- Library
- Theses
website: https://www.ukm.my/portal/
---
