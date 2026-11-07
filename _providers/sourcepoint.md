---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
api_count: 7
apis:
- baseURL: https://cdn.privacy-mgmt.com/consent/tcfv2
  baseurl_source: declared
  description: The GDPR reporting API API from Sourcepoint — 2 operation(s) for gdpr reporting api.
  name: Sourcepoint GDPR reporting API
  slug: sourcepoint-gdpr-reporting-api-api
- baseURL: https://cdn.privacy-mgmt.com/consent/tcfv2
  baseurl_source: declared
  description: The GDPR TCF end-user consent status API from Sourcepoint — 3 operation(s) for gdpr tcf end-user consent status.
  name: Sourcepoint GDPR TCF end-user consent status API
  slug: sourcepoint-gdpr-tcf-end-user-consent-status-api
- baseURL: https://cdn.privacy-mgmt.com/consent/tcfv2
  baseurl_source: declared
  description: The GDPR TCF vendor list API from Sourcepoint — 3 operation(s) for gdpr tcf vendor list.
  name: Sourcepoint GDPR TCF vendor list API
  slug: sourcepoint-gdpr-tcf-vendor-list-api
- baseURL: https://cdn.privacy-mgmt.com/consent/tcfv2
  baseurl_source: declared
  description: The Preferences end-user history API from Sourcepoint — 2 operation(s) for preferences end-user history.
  name: Sourcepoint Preferences end-user history API
  slug: sourcepoint-preferences-end-user-history-api
- baseURL: https://cdn.privacy-mgmt.com/consent/tcfv2
  baseurl_source: declared
  description: The U.S. Multi-State Privacy end-user consent status API from Sourcepoint — 3 operation(s) for u.s. multi-state privacy end-user consent status.
  name: Sourcepoint U.S. Multi-State Privacy end-user consent status API
  slug: sourcepoint-u-s-multi-state-privacy-end-user-consent-status-api
- baseURL: https://cdn.privacy-mgmt.com/consent/tcfv2
  baseurl_source: declared
  description: The U.S. Multi-State Privacy reporting API API from Sourcepoint — 2 operation(s) for u.s. multi-state privacy reporting api.
  name: Sourcepoint U.S. Multi-State Privacy reporting API
  slug: sourcepoint-u-s-multi-state-privacy-reporting-api-api
artifact_total: 42
collections:
- collection_type: open
  name: Sourcepoint GDPR Standard API
  slug: open-sourcepoint-gdpr-standard
- collection_type: open
  name: Sourcepoint GDPR TCF API
  slug: open-sourcepoint-gdpr-tcf
- collection_type: open
  name: Sourcepoint Global Enterprise API
  slug: open-sourcepoint-global-enterprise
- collection_type: open
  name: Preferences API
  slug: open-sourcepoint-preferences
- collection_type: open
  name: Sourcepoint Reporting GDPR API
  slug: open-sourcepoint-reporting-gdpr
- collection_type: open
  name: Sourcepoint Reporting U.S. Multi-State Privacy API
  slug: open-sourcepoint-reporting-usnat
- collection_type: open
  name: Sourcepoint U.S. Multi-State Privacy API
  slug: open-sourcepoint-usnat
common:
- group: other
  href: https://artifacts.apis.io/sourcepoint/capabilities/sourcepoint-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sourcepoint-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/sourcepoint/overlays/sourcepoint-gdpr-tcf-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sourcepoint-gdpr-tcf-overlay.yaml
- group: other
  href: https://artifacts.apis.io/sourcepoint/overlays/sourcepoint-gdpr-standard-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sourcepoint-gdpr-standard-overlay.yaml
- group: other
  href: https://artifacts.apis.io/sourcepoint/overlays/sourcepoint-usnat-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sourcepoint-usnat-overlay.yaml
- group: other
  href: https://artifacts.apis.io/sourcepoint/overlays/sourcepoint-global-enterprise-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sourcepoint-global-enterprise-overlay.yaml
- group: other
  href: https://artifacts.apis.io/sourcepoint/overlays/sourcepoint-preferences-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sourcepoint-preferences-overlay.yaml
- group: other
  href: https://artifacts.apis.io/sourcepoint/overlays/sourcepoint-reporting-gdpr-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sourcepoint-reporting-gdpr-overlay.yaml
- group: other
  href: https://artifacts.apis.io/sourcepoint/overlays/sourcepoint-reporting-usnat-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sourcepoint-reporting-usnat-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/sourcepoint/authentication/sourcepoint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sourcepoint-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sourcepoint/security/sourcepoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sourcepoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sourcepoint.com
- group: start
  title: ''
  type: Portal
  url: https://docs.sourcepoint.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://sourcepoint-public-api.readme.io/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/4416092045587-GDPR-TCF-implementation-guide-web
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/4405397484307-Event-callbacks-CMP
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/4405412419731-Client-configuration-parameters
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/4403274791699-Authenticated-consent
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/6490142709139-Native-App-Messages-App-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/25872524725267-Google-Consent-Mode-2-0-GDPR-TCF-web
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/cmp-2/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/diagnose/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/dsar/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/marketing-preferences/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/universal-consent-and-preferences
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/privacy-lens/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/ott-ctv/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/cmp-for-mobile-apps/
- group: commercial
  title: ''
  type: Pricing
  url: https://hs.sourcepoint.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.sourcepoint.com/schedule-a-demo/
- group: company
  title: ''
  type: Blog
  url: https://www.sourcepoint.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.sourcepoint.com/news/
- group: company
  title: ''
  type: About
  url: https://www.sourcepoint.com/about-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SourcePointUSA
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/ios-cmp-app
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/android-cmp-app
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/react-native-sourcepoint-cmp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/unity-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/sp-roku-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/SP_HTML5_OTT
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/mobile-core
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/diagnose-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/es3-QR-SDK-develop
- group: build
  title: ''
  type: Plugin
  url: https://github.com/SourcePointUSA/sp-wordpress-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/SourcePointUSA/sp-magento-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/SourcePointUSA/GTM-GCM-Template
- group: build
  title: ''
  type: Tools
  url: https://github.com/SourcePointUSA/sdks-auth-consent-test-page
- group: build
  title: ''
  type: Tools
  url: https://github.com/SourcePointUSA/FORK-iabgpp-es
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sourcepoint
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sourcepoint
- group: agent
  href: https://artifacts.apis.io/sourcepoint/llms/sourcepoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sourcepoint-llms.txt
- group: agent
  href: https://artifacts.apis.io/sourcepoint/well-known/sourcepoint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sourcepoint-well-known.yml
- group: other
  href: https://artifacts.apis.io/sourcepoint/well-known/sourcepoint-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/sourcepoint-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/sourcepoint/mcp/sourcepoint-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sourcepoint-mcp.yml
- group: build
  href: https://artifacts.apis.io/sourcepoint/mcp/sourcepoint-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sourcepoint-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/sourcepoint/packages/sourcepoint-packages.yml
  title: ''
  type: Packages
  url: packages/sourcepoint-packages.yml
- group: build
  href: https://artifacts.apis.io/sourcepoint/packages/sourcepoint-packages.yml
  title: ''
  type: SDKs
  url: packages/sourcepoint-packages.yml
- group: design
  href: https://artifacts.apis.io/sourcepoint/conformance/sourcepoint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sourcepoint-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.sourcepoint.com/trust-and-security/
- group: auth
  href: https://artifacts.apis.io/sourcepoint/security/sourcepoint-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sourcepoint-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sourcepoint/security/sourcepoint-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sourcepoint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sourcepoint.com/trust-and-security/
- group: design
  href: https://artifacts.apis.io/sourcepoint/errors/sourcepoint-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sourcepoint-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sourcepoint/lifecycle/sourcepoint-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sourcepoint-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sourcepoint/conventions/sourcepoint-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sourcepoint-conventions.yml
- group: operate
  href: https://artifacts.apis.io/sourcepoint/changelog/sourcepoint-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sourcepoint-changelog.yml
- group: design
  href: https://artifacts.apis.io/sourcepoint/components/sourcepoint-components.yml
  title: ''
  type: Components
  url: components/sourcepoint-components.yml
- group: design
  href: https://artifacts.apis.io/sourcepoint/data-model/sourcepoint-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sourcepoint-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/sourcepoint/plans/sourcepoint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sourcepoint-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sourcepoint/rate-limits/sourcepoint-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sourcepoint-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/sourcepoint/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://sourcepoint-public-api.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://sourcepoint-public-api.readme.io/reference/welcome-to-the-sourcepoint-api-hub
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.sourcepoint.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sourcepoint.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sourcepoint.com/privacy-policy/
- group: commercial
  title: ''
  type: PrivacyNotice
  url: https://www.sourcepoint.com/privacy-notice/
- group: start
  title: ''
  type: Login
  url: https://portal.sourcepoint.com
- group: company
  title: ''
  type: Press
  url: https://www.sourcepoint.com/press/
created: '2026-05-25'
description: Sourcepoint is a New York City-headquartered enterprise privacy and consent management technology company founded in 2015 by Ben Barokas and Brian Kane. The platform began as an ad-block recovery solution for publishers and evolved into a Consent Management Platform (CMP) used by leading global publishers and brands — including Axel Springer, Bauer Media, CNN International, Future, Haymarket, LADBible, Autotrader, and Ancestry — to handle GDPR, CCPA, U.S. Multi-State Privacy (USNAT), LGPD, and other regulations under the IAB TCF v2.2 and IAB Global Privacy Platform (GPP) frameworks. Sourcepoint products include the multi-campaign CMP across web, AMP, mobile (iOS, Android, React Native), Unity, Roku, HTML5 OTT and CTV surfaces, Compliance Monitoring (Diagnose), DSAR Handling, Universal Consent & Preferences, Marketing Preferences, Privacy Lens, and tooling for ad-block recovery. The Sourcepoint Public API exposes REST endpoints for GDPR TCF, GDPR Standard, U.S. Multi-State Privacy,
  Global Enterprise consent, and Preferences history, plus reporting endpoints for dashboards. Sourcepoint technology powers over 30 billion consumer touchpoints per month. In July 2025, Sourcepoint was acquired by Paris-based Didomi (a Marlin Equity Partners portfolio company) to consolidate global consent management; Sourcepoint continues to operate under its existing brand and developer surface during integration.
features:
- Multi-campaign Consent Management Platform across web, AMP, mobile, OTT, CTV, and gaming surfaces
- IAB TCF v2.2 support including Transaction Receipts, Legal Preferences, and sensitive-data opt-in
- IAB Global Privacy Platform (GPP) support for U.S. Multi-State Privacy (USNAT) sections
- GDPR, CCPA / U.S. Multi-State Privacy, LGPD, and global multi-regulation orchestration
- Universal Consent & Preferences for unified first-party preference data
- Authenticated Consent for syncing an end-user's preferences across devices
- Diagnose compliance monitoring of vendors, trackers, and data flows on a property
- DSAR Handling for data subject access and erasure workflows
- Marketing Preferences and Privacy Lens measurement
- Ad-block recovery heritage for publisher monetization
- Google Consent Mode 2.0 integration and GTM template
- Native mobile SDKs for iOS (Swift / CocoaPods / SPM / XCFramework), Android (Kotlin / Maven Central), React Native, Unity, Roku, and HTML5 OTT
- Web messaging via cdn.privacy-mgmt.com/unified/wrapperMessagingWithoutDetection.js with optional CNAME subdomain
- Public REST API for GDPR TCF, GDPR Standard, U.S. Multi-State Privacy, Global Enterprise, Preferences, and Reporting
- Approximately 30 billion consumer touchpoints powered per month
finops:
- has_sources: true
  method: derived
  name: Sourcepoint Finops
  primary_unit: subscription
  service_category: ''
  slug: sourcepoint-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sourcepoint.png
layout: provider
modified: '2026-08-12'
name: Sourcepoint
nav: Providers
network: true
overview: 'Sourcepoint publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including GDPR reporting API, GDPR TCF end-user consent status API, GDPR TCF vendor list API, and 3 more. Tagged areas include Privacy, Consent Management, Consent Management Platform, CMP, and GDPR.


  The Sourcepoint catalog on APIs.io includes 1 Spectral governance ruleset.


  Sourcepoint''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, engineering blog, product news, and 71 more developer resources.'
plans:
- name: Sourcepoint Plans Pricing
  plan_count: 3
  slug: sourcepoint-plans-pricing
- name: Sourcepoint Price Estimates
  plan_count: 0
  slug: sourcepoint-price-estimates
random_paper: 11
rate_limits:
- limit_count: 0
  name: Sourcepoint Rate Limits
  slug: sourcepoint-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Sourcepoint API Rules
  rule_count: 51
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 3
  slug: sourcepoint-rules
score:
  band: strong
  composite: 62.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 44.5
    developer_ergonomics: 74.4
    discoverability: 80.8
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
    - north-america
  previous_composite: 60.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sourcepoint/sourcepoint-2026-06-20T194225.png
security:
- kind: authentication
  name: Sourcepoint Authentication
  slug: sourcepoint-authentication
  summary_line: apiKey/none · 2 schemes
- kind: domain-security
  name: Sourcepoint Domain Security
  slug: sourcepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sourcepoint Vulnerability Disclosure
  slug: sourcepoint-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Sourcepoint Trust Center
  slug: sourcepoint-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701
skill_count: 5
skills:
- name: sourcepoint-consent-dashboard-reporting
  slug: sourcepoint-consent-dashboard-reporting
- name: sourcepoint-consent-status-lookup
  slug: sourcepoint-consent-status-lookup
- name: sourcepoint-dsar-consent-erasure
  slug: sourcepoint-dsar-consent-erasure
- name: sourcepoint-tcf-vendor-list-audit
  slug: sourcepoint-tcf-vendor-list-audit
- name: sourcepoint-usnat-opt-out
  slug: sourcepoint-usnat-opt-out
slug: sourcepoint
tags:
- Privacy
- Consent Management
- Consent Management Platform
- CMP
- GDPR
- CCPA
- LGPD
- IAB TCF
- IAB GPP
- USNAT
- DSAR
- Adblock Recovery
- Compliance Monitoring
- Publisher Technology
- AdTech
- MarTech
- Privacy Engineering
- CTV
- OTT
- Mobile SDK
- Web SDK
website: https://www.sourcepoint.com
---
