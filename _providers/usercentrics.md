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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Usercentrics Agentic Access
  operation_count: 29
  slug: usercentrics-agentic-access
  summary_line: 29 operations · 17 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: Hosted server-side Google Tag Manager service for first-party data collection, consent enforcement, and tag execution off the browser. Includes Meta Signals Gateway for the Meta Conversions API and co
  name: Usercentrics Server-Side Tagging (sGTM)
  slug: server-side-tagging
- description: The CCPA API from Usercentrics — 1 operation(s) for ccpa.
  name: Usercentrics CCPA API
  slug: usercentrics-ccpa-api
- description: The Consent API from Usercentrics — 11 operation(s) for consent.
  name: Usercentrics Consent API
  slug: usercentrics-consent-api
- description: The Consent Mode API from Usercentrics — 1 operation(s) for consent mode.
  name: Usercentrics Consent Mode API
  slug: usercentrics-consent-mode-api
- description: The Controller API from Usercentrics — 1 operation(s) for controller.
  name: Usercentrics Controller API
  slug: usercentrics-controller-api
- description: The Dialog API from Usercentrics — 3 operation(s) for dialog.
  name: Usercentrics Dialog API
  slug: usercentrics-dialog-api
- description: The GPP API from Usercentrics — 2 operation(s) for gpp.
  name: Usercentrics GPP API
  slug: usercentrics-gpp-api
- description: The Lifecycle API from Usercentrics — 4 operation(s) for lifecycle.
  name: Usercentrics Lifecycle API
  slug: usercentrics-lifecycle-api
- description: The Scanner API from Usercentrics — 1 operation(s) for scanner.
  name: Usercentrics Scanner API
  slug: usercentrics-scanner-api
- description: The TCF API from Usercentrics — 3 operation(s) for tcf.
  name: Usercentrics TCF API
  slug: usercentrics-tcf-api
- description: The UI API from Usercentrics — 2 operation(s) for ui.
  name: Usercentrics UI API
  slug: usercentrics-ui-api
artifact_total: 77
collections:
- collection_type: open
  name: Usercentrics App CMP SDK API
  slug: open-usercentrics-app-cmp-sdk
- collection_type: open
  name: Cookiebot CMP API
  slug: open-usercentrics-cookiebot-cmp
- collection_type: open
  name: Usercentrics Web CMP V3 API
  slug: open-usercentrics-web-cmp-v3
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usercentrics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usercentrics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usercentrics.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.usercentrics.com/
- group: start
  title: ''
  type: Signup
  url: https://usercentrics.com/free-trial/
- group: commercial
  title: ''
  type: Pricing
  url: https://usercentrics.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/usercentrics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usercentrics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usercentrics-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://usercentrics.com/knowledge-hub/
- group: operate
  title: ''
  type: Support
  url: https://support.usercentrics.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usercentrics.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usercentrics.com/terms-and-conditions/
- group: docs
  title: ''
  type: Documentation
  url: https://usercentrics.com/legal-documents/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Usercentrics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usercentrics/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cookiebot.com/en/
created: '2026-05-25'
description: Usercentrics is a Munich-based consent management platform (CMP) and privacy compliance provider. Founded in 2017 and led by CEO Donna Dror, Usercentrics acquired Danish CMP Cookiebot (Cybot) in September 2021 and acquired MCP Manager in January 2026. The platform serves 2.4M+ websites and apps across 195 countries, processing 8.8B+ monthly consents. Products span Web CMP, App CMP, CTV CMP, Server-Side Tagging, Meta Signals Gateway, Preference Manager, Privacy Policy Generator, Compliance Scanners, and MCP Manager for AI governance.
features:
- description: Browser-side consent management for GDPR, CCPA, TCF 2.3, GPP, and DMA.
  name: Web CMP
- description: Native and cross-platform mobile consent SDKs (iOS, Android, Flutter, React Native, Unity).
  name: App CMP
- description: Connected-TV and OTT consent SDKs for tvOS and AndroidTV.
  name: CTV CMP
- description: Patented monthly website scanner that auto-detects cookies and trackers.
  name: Cookiebot Scanner
- description: Hosted sGTM for consent-aware first-party data collection.
  name: Server-Side Tagging
- description: Server-side Meta Conversions API forwarding aligned with consent.
  name: Meta Signals Gateway
- description: First-party preference center for granular subscriber data.
  name: Preference Manager
- description: Automated, multi-language, multi-regulation privacy policy authoring.
  name: Privacy Policy Generator
- description: Web and App scanners for ongoing compliance monitoring.
  name: Compliance Scanners
- description: Governance platform for Model Context Protocol data access by AI agents.
  name: MCP Manager
- description: Native integration with Google's consent signaling for Ads, Analytics, and GTM.
  name: Google Consent Mode v2
- description: Full IAB Transparency and Consent Framework support for ad-tech consent strings.
  name: IAB TCF 2.3
- description: Global Privacy Platform support for multi-jurisdiction consent signaling.
  name: IAB GPP
- description: 47+ supported languages with geotargeted banners.
  name: Multi-Language
finops:
- name: Usercentrics Finops
  service_category: Privacy & Compliance
  slug: usercentrics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usercentrics.png
integrations:
- name: WordPress
- name: Shopify
- name: Wix
- name: HubSpot
- name: Square
- name: Duda
- name: Shopware
- name: eRecht24
- name: Joomla
- name: Webflow
- name: Squarespace
- name: GoDaddy
- name: Drupal
- name: TYPO3
- name: Magento
- name: WooCommerce
- name: Google Tag Manager
- name: Adobe Launch
- name: Google Ads (Consent Mode v2)
- name: Microsoft Advertising (UET Consent Mode)
- name: Meta Conversions API
- name: Flutter
- name: Unity Ads
- name: Adjust
- name: AppLovin
- name: ironSource
- name: Crashlytics
- name: Chartboost
- name: MineOS
- name: Kameleoon
- name: Optimizely
layout: provider
modified: '2026-05-25'
name: Usercentrics
nav: Providers
network: true
overview: 'Usercentrics publishes 10 APIs on the [APIs.io](https://apis.io/) network, including CCPA API, Consent API, Consent Mode API, and 7 more. Tagged areas include Privacy, Consent, CMP, Compliance, and GDPR.


  Usercentrics'' developer surface includes developer portal, signup flow, pricing, engineering blog, support, documentation, and 11 more developer resources.'
plans:
- name: Usercentrics Plans Pricing
  plan_count: 19
  slug: usercentrics-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 4
  name: Usercentrics Rate Limits
  slug: usercentrics-rate-limits
score:
  band: developing
  composite: 46.5
  delta: 2.1
  facets:
    commercial_clarity: 84.2
    contract_quality: 54.5
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usercentrics/refs/heads/main/screenshots/usercentrics-2026-06-20T200655.png
security:
- kind: domain-security
  name: Usercentrics Domain Security
  slug: usercentrics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: usercentrics
solutions:
- description: Self-serve consent for solopreneurs and emerging businesses.
  name: Cookiebot Core
- description: Enterprise CMP with advanced customization, A/B testing, and analytics.
  name: Usercentrics Advanced
- description: Custom-priced offering for Connected TV and OTT applications.
  name: TV Premium
- description: Enterprise App CMP with API access, white labeling, and dedicated CSE.
  name: App Premium
tags:
- Privacy
- Consent
- CMP
- Compliance
- GDPR
- CCPA
- TCF
- GPP
- Cookies
- AI Governance
use_cases:
- description: Consent for ad-funded media operating across multiple regulations.
  name: Media and Publishing
- description: Consent-aware tagging for first-party conversion measurement.
  name: Retail and Ecommerce
- description: Granular consent records and audit trails for regulated industries.
  name: Banking and Finance
- description: HIPAA-ready consent flows for patient-facing properties.
  name: Healthcare
- description: TCF-compliant consent in mobile games and Unity-based titles.
  name: Gaming
- description: Compliant consent collection for EdTech platforms and learner data.
  name: Education
- description: In-car and connected-vehicle consent capture.
  name: Automotive
- description: Multi-region consent for global booking and loyalty platforms.
  name: Travel and Hospitality
- description: MCP Manager governance of agent access to enterprise data.
  name: AI Governance
website: https://usercentrics.com/
---
