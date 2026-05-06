---
aid: ccpa
url: https://raw.githubusercontent.com/api-evangelist/ccpa/refs/heads/main/apis.yml
name: CCPA (California Consumer Privacy Act)
tags:
  - CPRA
  - California
  - Compliance
  - Data Protection
  - Data Subject Rights
  - Legal
  - Privacy
  - Regulation
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-04-23'
position: Consumer
description: 'The California Consumer Privacy Act (CCPA), amended by the California Privacy Rights Act (CPRA), is a state statute that grants California residents rights over their personal information: the right to know, delete, correct, opt-out of sale/sharing, limit use of sensitive personal information, and non-discrimination for exercising privacy rights. It is enforced by the California Privacy Protection Agency (CPPA) and the California Attorney General. Technical interoperability mechanisms include the Global Privacy Control (GPC) browser signal and the IAB Tech Lab US Privacy (USP) / Global Privacy Platform (GPP) signals for advertising technology. This index tracks the official regulatory resources, technical privacy signals, and commercial APIs that help businesses comply with CCPA/CPRA obligations.'
apis:
  - aid: ccpa:global-privacy-control
    name: Global Privacy Control (GPC) Specification
    tags:
      - Browser Signal
      - Opt-Out
      - Standard
    humanURL: https://globalprivacycontrol.org/
    properties:
      - url: https://globalprivacycontrol.org/
        type: Website
      - url: https://privacycg.github.io/gpc-spec/
        type: Specification
      - url: https://github.com/privacycg/gpc-spec
        type: SourceCode
    description: Global Privacy Control is a browser-level signal that communicates a user's opt-out preference to websites. The California Attorney General has affirmed that GPC must be treated as a valid CCPA "Do Not Sell or Share" opt-out request.
  - aid: ccpa:iab-gpp
    name: IAB Tech Lab Global Privacy Platform (GPP)
    tags:
      - AdTech
      - Consent
      - IAB
      - Signals
    humanURL: https://iabtechlab.com/gpp/
    properties:
      - url: https://iabtechlab.com/gpp/
        type: Documentation
      - url: https://github.com/InteractiveAdvertisingBureau/Global-Privacy-Platform
        type: SourceCode
      - url: https://github.com/InteractiveAdvertisingBureau/USPrivacy
        type: LegacySpec
    description: The IAB Tech Lab Global Privacy Platform (GPP) is the successor to the US Privacy (USP) string. It provides a standardized way to communicate user consent and opt-out signals between publishers, consent management platforms, and adtech vendors for CCPA, CPRA, and other jurisdictions.
  - aid: ccpa:cppa-enforcement-resources
    name: California Privacy Protection Agency (CPPA) Resources
    tags:
      - Enforcement
      - Regulation
      - Rulemaking
    humanURL: https://cppa.ca.gov/
    properties:
      - url: https://cppa.ca.gov/
        type: Website
      - url: https://cppa.ca.gov/regulations/
        type: Regulations
      - url: https://cppa.ca.gov/enforcement/
        type: Enforcement
    description: Official resources from the California Privacy Protection Agency, the body empowered by CPRA to implement, enforce, and publish regulations under the CCPA.
  - aid: ccpa:ca-data-broker-registry
    name: California Data Broker Registry
    tags:
      - Data Brokers
      - Registry
    humanURL: https://oag.ca.gov/data-brokers
    properties:
      - url: https://oag.ca.gov/data-brokers
        type: Registry
      - url: https://oag.ca.gov/data-brokers/submit
        type: Registration
    description: Official California Attorney General registry of data brokers required to register under Civil Code section 1798.99.80, providing a public list that consumers can use to submit opt-out requests.
common:
  - type: Website
    url: https://oag.ca.gov/privacy/ccpa
  - type: Documentation
    url: https://oag.ca.gov/privacy/ccpa
  - type: Regulator
    url: https://cppa.ca.gov/
  - type: StatuteText
    url: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=1.81.5.&part=4.&chapter=&article=
  - type: Regulations
    url: https://cppa.ca.gov/regulations/
  - type: FAQ
    url: https://oag.ca.gov/privacy/ccpa
  - type: Enforcement
    url: https://cppa.ca.gov/enforcement/
  - type: DataBrokerRegistry
    url: https://oag.ca.gov/data-brokers
  - type: GPC
    url: https://globalprivacycontrol.org/
  - type: GPP
    url: https://iabtechlab.com/gpp/
  - name: Rights
    type: Rights
    data:
      - name: Right to Know
      - name: Right to Delete
      - name: Right to Correct
      - name: Right to Opt-Out of Sale
      - name: Right to Opt-Out of Sharing (Cross-Context Behavioral Advertising)
      - name: Right to Limit Use of Sensitive Personal Information
      - name: Right to Data Portability
      - name: Right to Non-Discrimination
  - name: Applicability
    type: Applicability
    data:
      - name: Gross Annual Revenue > $25M
      - name: Personal Information of 100k+ California Residents
      - name: 50%+ Revenue From Sale of Personal Information
  - name: Features
    type: Features
    data:
      - name: Notice at Collection
      - name: Privacy Policy Disclosure
      - name: Do Not Sell or Share Link
      - name: Limit Use of Sensitive PI Link
      - name: Verifiable Consumer Requests
      - name: Authorized Agent Requests
      - name: Opt-Out Preference Signal (GPC)
      - name: Service Provider / Contractor Contracts
      - name: Data Processing Addendum
      - name: Data Retention Disclosure
      - name: Risk Assessments (CPRA)
      - name: Cybersecurity Audits (CPRA)
      - name: Automated Decision-Making Disclosures (CPRA)
  - name: UseCases
    type: UseCases
    data:
      - name: DSAR (Data Subject Access Request) Automation
      - name: Consent Management Platform (CMP)
      - name: Cookie Banner and Preference Center
      - name: Data Inventory and Mapping
      - name: Vendor Risk Management
      - name: Privacy Impact Assessments
      - name: Audit and Reporting
      - name: Global Privacy Control Handling
      - name: Data Broker Registration
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
