---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-04'
api_count: 10
apis:
- description: Hokkaido University's own Shibboleth/SAML 2.0 identity provider, entityID https://shib-idp01.iic.hokudai.ac.jp/idp/shibboleth, scope hokudai.ac.jp, registered in the GakuNin national academic federati
  name: Hokkaido University SAML 2.0 Identity Provider
  slug: saml-idp
- description: Membership of GakuNin (学術認証フェデレーション), the Japanese national academic identity federation operated by the National Institute of Informatics. The aggregate at metadata.gakunin.nii.ac.jp carries 650 enti
  name: GakuNin Academic Access Management Federation
  slug: gakunin
- description: Publicly crawlable XML sitemap index for HUSCAP, the Hokkaido University Collection of Scholarly and Academic Papers, providing a machine-readable list of repository item URLs across seven child sitem
  name: HUSCAP XML Sitemaps
  slug: huscap-sitemap
- description: XML sitemaps for the university's two public web estates — the 2.4 MB sitemap.xml on the Japanese site and the WordPress core sitemap index on the English global site. Machine-readable and institution
  name: Hokkaido University Web Sitemaps
  slug: web-sitemaps
- description: Hokkaido University Library holds Handle System naming authority prefix 2115, which mints the persistent identifiers on every HUSCAP record (hdl.handle.net/2115/…). Registered since 2005 and administr
  name: Handle System Prefix 2115
  slug: handle-2115
- description: 'Hokkaido University registers DOIs through JaLC, the Japan Link Center, under prefix 10.14943. Confirmed from the DOI Registration Agency resolver (doi.org/doiRA/10.14943 returns RA "JaLC"), from the '
  name: JaLC DOI Prefix 10.14943
  slug: jalc-doi-10-14943
- description: Research Organization Registry record https://ror.org/02e16g702, types education and funder, established 1876, located Sapporo, Japan. Carries the university's cross-registry identifiers — Crossref Fu
  name: ROR Registry Record
  slug: ror
- description: 'Crossref membership held at department level, not institution level. Member 5618, "Department of Mathematics, Hokkaido University", prefix 10.14492, 1,820 registered DOIs. Recorded because it is real '
  name: Crossref Member 5618 — Department of Mathematics
  slug: crossref-5618
- description: Public course catalog and syllabus search, institution-operated on the gakumu.academic.hokudai.ac.jp host. Live and open to the public, but web-only — an ASP.NET WebForms application with no documente
  name: Hokkaido University Syllabus Search (学務システム)
  slug: syllabus
- description: The Information Initiative Center's supercomputer and research cloud service — Grand Chariot 2 and the research cloud system — documented in Japanese and English with a published application and alloc
  name: Interdisciplinary Large-scale Computing System (HUCC)
  slug: hucc
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.hokudai.ac.jp/
- group: company
  title: ''
  type: About
  url: https://www.global.hokudai.ac.jp/about/
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.lib.hokudai.ac.jp/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.lib.hokudai.ac.jp/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://gakumu.academic.hokudai.ac.jp/Portal/Public/Syllabus/SearchMain.aspx
- group: other
  title: ''
  type: IdentityFederation
  url: https://aidipigakunin2.oicte.hokudai.ac.jp/saml/saml2/idp/metadata.php
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.hucc.hokudai.ac.jp/en/overview/ilcs/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.open-ed.hokudai.ac.jp/%E6%9C%AA%E5%88%86%E9%A1%9E/31-3.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.global.hokudai.ac.jp/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.lib.hokudai.ac.jp/support/huscap/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/hokkaidouni/
- group: auth
  title: ''
  type: Authentication
  url: authentication/hokkaido-saml-idp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hokkaido-conformance.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hokkaido-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hokkaido-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hokkaido-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hokkaido-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hokkaido-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ProductPage
  url: https://eprints.lib.hokudai.ac.jp/
created: '2026-06-03'
description: 'Hokkaido University (北海道大学) is a national research university in Sapporo, Japan, founded in 1876 as Sapporo Agricultural College, a member of Japan''s Designated National University group and ranked #173 in the QS World University Rankings 2025. It operates 12 undergraduate schools, 21 graduate schools and numerous research institutes. Its public programmable footprint is small and honest: the university publishes no developer portal, no API gateway and no documented public REST API — api., data., opendata., developer. and status.hokudai.ac.jp all fail to resolve, and the WordPress REST API on its English site is explicitly disabled. What it does operate, and what this profile is built on, is scholarly identity infrastructure. It runs its own SAML 2.0 / Shibboleth identity provider registered in GakuNin, the Japanese national academic access federation; it holds Handle System prefix 2115 and JaLC DOI prefix 10.14943 for the HUSCAP institutional repository; and it publishes
  crawlable XML sitemaps for both HUSCAP and its main web estate. HUSCAP''s OAI-PMH endpoint is the one real regression: IRDB still harvests the repository by OAI-PMH, but no base URL has been publicly documented since the December 2025 platform migration and eighteen candidate paths were probed unsuccessfully.'
finops:
- name: Hokkaido Finops
  service_category: Education
  slug: hokkaido-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hokkaido.png
jsonld:
- class_count: 10
  name: Hokkaido Context
  property_count: 5
  slug: hokkaido-context
layout: provider
modified: '2026-09-01'
name: Hokkaido University
nav: Providers
network: true
overview: 'Hokkaido University publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Japan, and National University.


  The Hokkaido University catalog on APIs.io includes 1 JSON-LD context.


  Hokkaido University''s developer surface includes support, authentication, and 18 more developer resources.'
plans:
- name: Hokkaido Plans Pricing
  plan_count: 2
  slug: hokkaido-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Hokkaido Rate Limits
  slug: hokkaido-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 17.3
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hokkaido/refs/heads/main/screenshots/hokkaido-2026-06-20T182813.png
security:
- kind: domain-security
  name: Hokkaido Domain Security
  slug: hokkaido-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hokkaido
tags:
- Education
- Higher Education
- University
- Japan
- National University
- Research
- Open Access
- Institutional Repository
- Identity Federation
- Shibboleth
- Research Computing
- Course Catalog
- Persistent Identifiers
website: https://www.hokudai.ac.jp/
---
