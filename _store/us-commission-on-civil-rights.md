---
aid: us-commission-on-civil-rights
url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-civil-rights/refs/heads/main/apis.yml
apis:
  - aid: us-commission-on-civil-rights:us-commission-on-civil-rights
    name: US Commission on Civil Rights
    tags:
      - Civil Rights
      - Federal Government
    humanURL: https://www.usccr.gov/
    properties:
      - url: https://www.usccr.gov/
        type: Documentation
      - url: https://www.usccr.gov/reports/data-inventory-program
        type: DataAPI
        title: Data Inventory Program
      - url: https://www.usccr.gov/reports/civil-rights-complaints
        type: DataAPI
        title: Civil Rights Complaints Interactive Map and Datasets
      - url: https://www.usccr.gov/reports/no-fear-act
        type: DataAPI
        title: No FEAR Act Statistics
      - url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-civil-rights/refs/heads/main/json-schema/us-commission-on-civil-rights-complaint-schema.json
        type: JSONSchema
        title: Civil Rights Complaint Schema
      - url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-civil-rights/refs/heads/main/json-schema/us-commission-on-civil-rights-report-schema.json
        type: JSONSchema
        title: Civil Rights Report Schema
      - url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-civil-rights/refs/heads/main/json-schema/us-commission-on-civil-rights-no-fear-act-schema.json
        type: JSONSchema
        title: No FEAR Act Statistic Schema
    description: The US Commission on Civil Rights is an independent, bipartisan federal agency established in 1957 that investigates, reports on, and issues public service announcements about discrimination or denials of equal protection based on race, color, religion, sex, age, disability, national origin, or in the electoral process. The Commission informs the development of national civil rights policy through research, advisory committees, and public reporting.
name: US Commission on Civil Rights
tags:
  - Civil Rights
  - Federal Government
  - Equal Protection
  - Discrimination
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-25'
modified: '2026-05-03'
position: Consumer
description: The US Commission on Civil Rights is an independent, bipartisan federal agency that investigates, reports on, and issues public service announcements about discrimination or denials of equal protection based on race, color, religion, sex, age, disability, national origin, or in the electoral process. The Commission informs the development of national civil rights policy and laws through factual research, advisory committees in all 50 states, and public reporting to the President and Congress.
common:
  - type: Website
    url: https://www.usccr.gov/
  - type: Documentation
    url: https://www.usccr.gov/reports
    title: Reports and Publications
  - type: FAQ
    url: https://www.usccr.gov/about/faq
    title: Frequently Asked Questions
  - type: TermsOfService
    url: https://www.usccr.gov/about/privacy-policy
    title: Privacy Policy
  - type: Contact
    url: https://www.usccr.gov/about/contact
    title: Contact Us
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-civil-rights/refs/heads/main/vocabulary/us-commission-on-civil-rights-vocabulary.yml
    title: US Commission on Civil Rights Vocabulary
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-civil-rights/refs/heads/main/json-ld/us-commission-on-civil-rights-context.jsonld
    title: US Commission on Civil Rights JSON-LD Context
  - type: Features
    data:
      - name: Civil Rights Complaints Data
        description: Interactive map and datasets of civil rights complaints filed with federal agencies, organized by state and subject matter.
      - name: Data Inventory Program
        description: Annual comprehensive data inventory maintained per the Foundations for Evidence-Based Policymaking Act of 2018, with a designated Chief Data Officer.
      - name: No FEAR Act Statistics
        description: Federal employee discrimination complaint statistics required under the Notification and Federal Employee Antidiscrimination and Retaliation Act.
      - name: Advisory Committee Reports
        description: Reports from 51 state and local advisory committees covering civil rights conditions across all 50 states and the District of Columbia.
      - name: Statutory Enforcement Reports
        description: Congressional and Presidential reports on federal agency civil rights enforcement activities and compliance.
  - type: UseCases
    data:
      - name: Civil Rights Policy Research
        description: Accessing Commission reports, briefing papers, and findings to inform civil rights policy development and legislative analysis.
      - name: Discrimination Complaint Analysis
        description: Analyzing civil rights complaint data by state, subject, and federal agency to understand discrimination patterns and trends.
      - name: Federal Agency Compliance Monitoring
        description: Reviewing No FEAR Act statistics and statutory enforcement data to assess federal agency compliance with civil rights laws.
      - name: Academic Research
        description: Using Commission datasets and reports for academic research on civil rights, equal opportunity, and discrimination in the United States.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
