---
aid: cybersecurity-and-infrastructure-security-agency
name: Cybersecurity and Infrastructure Security Agency
x-type: government
description: The Cybersecurity and Infrastructure Security Agency (CISA) is the United States federal civilian cybersecurity agency, part of the Department of Homeland Security. CISA reduces cybersecurity and physical security risk for the nation, coordinates federal civilian cyber defense, and partners with state, local, tribal, and territorial governments and the private sector. CISA publishes a number of public, unauthenticated machine-readable feeds, including the Known Exploited Vulnerabilities (KEV) catalog (mandatorily remediated by federal civilian agencies under Binding Operational Directive 22-01), Cybersecurity Advisories, and Common Security Advisory Framework (CSAF) advisories. CISA also operates an Automated Indicator Sharing (AIS) TAXII 2.1 server that delivers STIX cyber threat indicators to vetted partners under a Terms of Use and Interconnection Agreement.
url: https://raw.githubusercontent.com/api-evangelist/cybersecurity-and-infrastructure-security-agency/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Advisories
  - AIS
  - Binding Operational Directive
  - CSAF
  - CVE
  - CWE
  - Cybersecurity
  - Federal Government
  - Government
  - ICS-CERT
  - Information Sharing
  - KEV
  - Known Exploited Vulnerabilities
  - Risk Management
  - Security
  - STIX
  - TAXII
  - Threat Intelligence
  - Vulnerability Management
apis:
  - aid: cybersecurity-and-infrastructure-security-agency:kev
    name: CISA Known Exploited Vulnerabilities (KEV) Catalog
    description: The KEV catalog is CISA's authoritative list of vulnerabilities actively exploited in the wild. The full catalog is published as JSON and CSV at cisa.gov/sites/default/files/feeds, mirrored on GitHub at cisagov/kev-data, and accompanied by a versioned JSON Schema. Federal civilian agencies must remediate KEV entries by the per-entry dueDate under BOD 22-01.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
    baseURL: https://www.cisa.gov
    tags:
      - BOD 22-01
      - CVE
      - CWE
      - Federal Government
      - JSON Feed
      - KEV
      - Vulnerability Management
    properties:
      - type: Documentation
        url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
      - type: JSONFeed
        url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
      - type: CSVFeed
        url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.csv
      - type: JSONSchema
        url: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities_schema.json
      - type: GitHubMirror
        url: https://github.com/cisagov/kev-data
      - type: OpenAPI
        url: openapi/cisa-kev-openapi.yml
      - type: Capabilities
        url: capabilities/cisa-kev-capabilities.yml
      - type: Rules
        url: rules/cisa-kev-rules.yml
  - aid: cybersecurity-and-infrastructure-security-agency:ais
    name: CISA Automated Indicator Sharing (AIS) TAXII Server
    description: CISA's Automated Indicator Sharing (AIS) program uses a TAXII 2.1 server to deliver STIX-formatted cyber threat indicators (CTI) and defensive measures (DM) to vetted partners. AIS includes AIS PUBLIC, FEDGOV, and CISCP feed communities. Connection requires a static IP, a Terms of Use, and an Interconnection Agreement; commercial data aggregators also redistribute AIS content to subscribers.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/automated-indicator-sharing-ais
    tags:
      - AIS
      - Information Sharing
      - STIX
      - TAXII
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/automated-indicator-sharing-ais
      - type: ConnectionGuide
        url: https://www.cisa.gov/resources-tools/resources/automated-indicator-sharing-ais-taxii-server-connection-guide
      - type: TAXIIDocumentation
        url: https://www.cisa.gov/automated-indicator-sharing-ais-20-documents-more-information
  - aid: cybersecurity-and-infrastructure-security-agency:advisories
    name: CISA Cybersecurity Advisories
    description: CISA publishes Cybersecurity Advisories (CSAs), Industrial Control Systems Advisories (ICSAs), and Common Security Advisory Framework (CSAF) JSON documents describing tactics, techniques, indicators, and required mitigations for active threats. Advisories are browsable on cisa.gov and many are exported as machine-readable CSAF JSON.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cisa.gov/news-events/cybersecurity-advisories
    tags:
      - Advisories
      - CSAF
      - ICS-CERT
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://www.cisa.gov/news-events/cybersecurity-advisories
      - type: ICSAdvisories
        url: https://www.cisa.gov/news-events/ics-advisories
      - type: CSAF
        url: https://www.cisa.gov/news-events/cybersecurity-advisories/csaf
common:
  - type: Website
    url: https://www.cisa.gov
  - type: KEVCatalog
    url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - type: Advisories
    url: https://www.cisa.gov/news-events/cybersecurity-advisories
  - type: Topics
    url: https://www.cisa.gov/topics
  - type: ResourcesAndTools
    url: https://www.cisa.gov/resources-tools
  - type: NewsAndEvents
    url: https://www.cisa.gov/news-events
  - type: GitHubOrganization
    url: https://github.com/cisagov
  - type: KEVDataMirror
    url: https://github.com/cisagov/kev-data
  - type: ContactUs
    url: https://www.cisa.gov/about/contact-us
  - type: PrivacyPolicy
    url: https://www.cisa.gov/privacy-policy
  - type: JSON-LD
    url: json-ld/cisa-context.jsonld
  - type: JSONSchema
    url: json-schema/cisa-kev-vulnerability-schema.json
  - type: Vocabulary
    url: vocabulary/cisa-vocabulary.yml
  - type: Capabilities
    url: capabilities/cisa-kev-capabilities.yml
  - type: Rules
    url: rules/cisa-kev-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
