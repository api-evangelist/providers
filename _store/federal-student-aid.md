---
aid: federal-student-aid
name: Federal Student Aid
description: The Federal Student Aid (FSA) office of the U.S. Department of Education provides grants, loans, and work-study funds to eligible students enrolled in college or career school. FSA operates StudentAid.gov as the consumer portal for managing federal student loans, completing the FAFSA, and exploring repayment options. FSA does not currently publish a public, open developer API program; aggregate higher education and aid data is redistributed through the Department of Education's open data programs such as the College Scorecard API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Education
  - Federal Government
  - Financial Aid
  - Grants
  - Loans
  - Student Aid
url: https://raw.githubusercontent.com/api-evangelist/federal-student-aid/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-student-aid:studentaid-gov
    name: StudentAid.gov
    description: StudentAid.gov is the official consumer platform for U.S. federal student aid. Borrowers and students use the site to complete the FAFSA, manage federal loans, review repayment plans, and access aid resources. The platform itself is not exposed as a public REST API today.
    humanURL: https://studentaid.gov
    tags:
      - Financial Aid
      - Loans
      - Student Aid
    properties:
      - type: Website
        url: https://studentaid.gov
      - type: FAFSA
        url: https://studentaid.gov/h/apply-for-aid/fafsa
      - type: Loan Repayment
        url: https://studentaid.gov/manage-loans/repayment
  - aid: federal-student-aid:college-scorecard
    name: College Scorecard API
    description: The College Scorecard API, operated by the U.S. Department of Education via api.data.gov, exposes institution-level data including federal aid participation, costs, completion rates, and post-college outcomes that complement Federal Student Aid program information.
    humanURL: https://collegescorecard.ed.gov/data/documentation/
    baseURL: https://api.data.gov/ed/collegescorecard/v1
    tags:
      - Education
      - Open Data
      - Higher Education
    properties:
      - type: Documentation
        url: https://collegescorecard.ed.gov/data/documentation/
      - type: Sign Up
        url: https://api.data.gov/signup/
common:
  - type: Website
    url: https://studentaid.gov
  - type: About
    url: https://studentaid.gov/about
  - type: FAFSA
    url: https://studentaid.gov/h/apply-for-aid/fafsa
  - type: Open Data
    url: https://www.ed.gov/about/news/data
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
