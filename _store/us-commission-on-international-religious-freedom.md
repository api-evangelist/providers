---
aid: us-commission-on-international-religious-freedom
url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-international-religious-freedom/refs/heads/main/apis.yml
apis:
  - aid: us-commission-on-international-religious-freedom:us-commission-on-international-religious-freedom
    name: US Commission on International Religious Freedom
    tags:
      - Federal Government
      - Religious Freedom
      - International Human Rights
    humanURL: https://www.uscirf.gov/
    properties:
      - url: https://www.uscirf.gov/
        type: Documentation
      - url: https://www.uscirf.gov/annual-reports
        type: DataAPI
        title: Annual Reports Archive
      - url: https://www.uscirf.gov/countries/2026-annual-report
        type: DataAPI
        title: 2026 Annual Report Country Assessments
      - url: https://www.uscirf.gov/countries/2026-recommendations
        type: DataAPI
        title: 2026 Country Recommendations
      - url: https://www.uscirf.gov/publications
        type: DataAPI
        title: Publications and Research
      - url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-international-religious-freedom/refs/heads/main/json-schema/uscirf-country-assessment-schema.json
        type: JSONSchema
        title: Country Assessment Schema
      - url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-international-religious-freedom/refs/heads/main/json-schema/uscirf-annual-report-schema.json
        type: JSONSchema
        title: Annual Report Schema
      - url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-international-religious-freedom/refs/heads/main/json-schema/uscirf-policy-recommendation-schema.json
        type: JSONSchema
        title: Policy Recommendation Schema
    description: The US Commission on International Religious Freedom (USCIRF) is an independent, bipartisan federal government commission created by the International Religious Freedom Act of 1998 that monitors religious freedom violations abroad and makes policy recommendations to the President, Secretary of State, and Congress. USCIRF designates Countries of Particular Concern (CPCs), Special Watch List (SWL) countries, and Entities of Particular Concern (EPCs) based on systematic, ongoing, egregious violations of religious freedom.
name: US Commission on International Religious Freedom
tags:
  - Federal Government
  - Religious Freedom
  - International Human Rights
  - Foreign Policy
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-25'
modified: '2026-05-03'
position: Consumer
description: The US Commission on International Religious Freedom (USCIRF) is an independent, bipartisan federal government commission created by the International Religious Freedom Act (IRFA) of 1998. USCIRF monitors the universal right to freedom of religion or belief abroad, reviews the facts and circumstances of violations of religious freedom internationally, and makes policy recommendations to the President, Secretary of State, and Congress. The Commission publishes an annual report designating Countries of Particular Concern (CPCs) and Special Watch List (SWL) countries, and recommends Entities of Particular Concern (EPCs) among non-state actors.
common:
  - type: Website
    url: https://www.uscirf.gov/
  - type: Documentation
    url: https://www.uscirf.gov/publications
    title: Publications
  - type: Documentation
    url: https://www.uscirf.gov/annual-reports
    title: Annual Reports Archive
  - type: Contact
    url: https://www.uscirf.gov/about-uscirf/contact-us
    title: Contact USCIRF
  - type: TermsOfService
    url: https://www.uscirf.gov/privacy-policy
    title: Privacy Policy
  - type: Features
    data:
      - name: Annual Report
        description: Comprehensive annual report documenting religious freedom conditions in countries worldwide, with CPC and SWL designations and policy recommendations to the U.S. government.
      - name: Countries of Particular Concern Designations
        description: Formal designation recommendations for countries that engage in or tolerate particularly severe violations of religious freedom, used to guide U.S. foreign policy.
      - name: Special Watch List
        description: Countries that do not meet the CPC threshold but require close monitoring due to severe violations of religious freedom.
      - name: Entities of Particular Concern
        description: Non-state actor designations for groups that engage in particularly severe violations of religious freedom abroad.
      - name: Country Reports and Fact Sheets
        description: Detailed country-by-country assessments of religious freedom conditions, minority group situations, and government treatment of religious communities.
      - name: Policy Briefs and Recommendations
        description: Targeted policy recommendations on specific issues, countries, or legislation for the President, Secretary of State, and Congress.
  - type: UseCases
    data:
      - name: Foreign Policy Analysis
        description: Using USCIRF designations and reports to understand U.S. government positions on international religious freedom and foreign policy priorities.
      - name: Country Risk Assessment
        description: Assessing religious freedom risks in specific countries using CPC, SWL, and country report data for diplomatic, humanitarian, or business purposes.
      - name: Human Rights Research
        description: Academic and advocacy research on international religious freedom conditions, trends, and the effectiveness of U.S. policy interventions.
      - name: Refugee and Asylum Applications
        description: Using USCIRF country assessments as supporting documentation for asylum claims and refugee status determinations involving religious persecution.
      - name: Congressional and Policy Advocacy
        description: Informing legislative advocacy and policy development using USCIRF recommendations and findings on specific countries or religious freedom issues.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-international-religious-freedom/refs/heads/main/vocabulary/us-commission-on-international-religious-freedom-vocabulary.yml
    title: USCIRF Vocabulary
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-international-religious-freedom/refs/heads/main/json-ld/us-commission-on-international-religious-freedom-context.jsonld
    title: USCIRF JSON-LD Context
  - type: Integrations
    data:
      - name: U.S. Department of State
        description: USCIRF works with the State Department's Office of International Religious Freedom, and State uses USCIRF recommendations for CPC and SWL designations.
      - name: U.S. Congress
        description: USCIRF reports directly to Congress, submitting annual and special reports with legislative recommendations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
