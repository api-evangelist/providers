---
aid: chief-financial-officers-council
url: https://raw.githubusercontent.com/api-evangelist/chief-financial-officers-council/refs/heads/main/apis.yml
name: Chief Financial Officers Council
tags:
  - Federal Financial Management
  - Federal Government
  - Finance
  - Government
  - OMB
  - Treasury
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: The Chief Financial Officers Council (CFOC) was established by the Chief Financial Officers (CFO) Act of 1990 (Public Law 101-576) and is composed of the CFOs and Deputy CFOs of the 24 largest federal departments and agencies, along with senior officials from the Office of Management and Budget (OMB) and the Department of the Treasury. The Council works collaboratively to improve federal financial management through shared guidance, working groups, and inter-agency standards. While the CFO Council itself does not operate a developer API program, its remit is closely tied to the larger ecosystem of federal financial management data and APIs administered by Treasury (USAspending.gov, Fiscal Service), OMB (PaymentAccuracy.gov, MAX.gov), and GSA (Performance.gov, SAM.gov).
apis:
  - aid: chief-financial-officers-council:cfoc-website
    name: CFO Council Website
    tags:
      - Council
      - Federal Financial Management
      - Resources
    humanURL: https://www.cfo.gov/
    properties:
      - url: https://www.cfo.gov/
        type: Website
      - url: https://www.cfo.gov/about-the-council/
        type: About
      - url: https://www.cfo.gov/resources/
        type: Resources
    description: The cfo.gov public website is the official portal for the federal CFO Council, hosting member rosters, council news, working-group outputs, financial-management policy guidance, and links to companion federal financial-management resources.
  - aid: chief-financial-officers-council:cfoc-working-groups
    name: CFO Council Working Groups
    tags:
      - Inter-Agency
      - Standards
      - Working Groups
    humanURL: https://www.cfo.gov/working-groups/
    properties:
      - url: https://www.cfo.gov/working-groups/
        type: Website
    description: The CFO Council operates topical working groups covering areas such as financial systems, internal control, grants management, payment integrity, financial reporting, and data analytics. Working-group products including white papers, playbooks, and recommended practices are published on cfo.gov.
  - aid: chief-financial-officers-council:cfoc-payment-integrity
    name: PaymentAccuracy.gov (Payment Integrity)
    tags:
      - Improper Payments
      - Open Data
      - Payment Integrity
    humanURL: https://www.paymentaccuracy.gov/
    properties:
      - url: https://www.paymentaccuracy.gov/
        type: Website
      - url: https://www.paymentaccuracy.gov/payment-accuracy-the-numbers/
        type: Data
    description: PaymentAccuracy.gov is the OMB-maintained transparency site for reporting government-wide improper payments and payment-integrity activities. The site publishes downloadable agency-level payment accuracy datasets that are referenced and used by CFO Council members for benchmarking.
  - aid: chief-financial-officers-council:usaspending
    name: USAspending.gov API (Treasury)
    tags:
      - Federal Spending
      - Open Data
      - Treasury
    humanURL: https://api.usaspending.gov/
    properties:
      - url: https://api.usaspending.gov/
        type: Website
      - url: https://api.usaspending.gov/docs/endpoints
        type: Documentation
      - url: https://api.usaspending.gov/api/v2/
        type: BaseURL
    description: USAspending.gov is the Treasury-operated public source of accountable federal spending data, exposing a comprehensive REST API for federal awards, contracts, grants, sub-awards, and agency budget data. CFO Council members rely on USAspending data quality and standards (DAIMS) for transparency reporting.
  - aid: chief-financial-officers-council:max-gov
    name: MAX.gov / Performance.gov
    tags:
      - Performance Management
      - Treasury Performance
    humanURL: https://www.performance.gov/
    properties:
      - url: https://www.performance.gov/
        type: Website
      - url: https://www.performance.gov/about/
        type: About
    description: Performance.gov is the OMB-administered public site for federal cross-agency priority goals, agency strategic plans, and performance reports. The CFO Council collaborates with OMB on financial-management Cross-Agency Priority (CAP) goals reported through Performance.gov.
common:
  - type: Website
    url: https://www.cfo.gov/
  - type: About
    url: https://www.cfo.gov/about-the-council/
  - type: Resources
    url: https://www.cfo.gov/resources/
  - type: WorkingGroups
    url: https://www.cfo.gov/working-groups/
  - type: News
    url: https://www.cfo.gov/news/
  - type: Events
    url: https://www.cfo.gov/events/
  - type: Members
    url: https://www.cfo.gov/members/
  - type: Contact
    url: mailto:CFOC.support@gsa.gov
  - type: Privacy Policy
    url: https://www.cfo.gov/privacy-policy/
  - type: AccessibilityStatement
    url: https://www.cfo.gov/accessibility/
  - type: USAspending
    url: https://www.usaspending.gov/
  - type: PaymentAccuracy
    url: https://www.paymentaccuracy.gov/
  - type: PerformanceGov
    url: https://www.performance.gov/
  - type: OMB
    url: https://www.whitehouse.gov/omb/
  - type: Treasury
    url: https://home.treasury.gov/
  - type: GSA
    url: https://www.gsa.gov/
  - name: ProgramAreas
    type: ProgramAreas
    data:
      - name: Federal Financial Management
      - name: Financial Reporting
      - name: Internal Controls
      - name: Payment Integrity
      - name: Improper Payments
      - name: Grants Management
      - name: Financial Systems
      - name: Workforce Development
      - name: Data Standards (DAIMS)
      - name: Cross-Agency Priority Goals
  - name: WorkingGroups
    type: WorkingGroups
    data:
      - name: Financial Management Workforce
      - name: Financial Systems
      - name: Grants Policy
      - name: Internal Control
      - name: Payment Integrity
      - name: Performance and Accountability
      - name: Financial Reporting
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
