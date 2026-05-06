---
aid: army-national-guard
url: https://raw.githubusercontent.com/api-evangelist/army-national-guard/refs/heads/main/apis.yml
name: Army National Guard
tags:
  - Federal Government
  - Military
  - Defense
  - National Guard
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-19'
description: The Army National Guard is a reserve component of the United States Army that serves both the nation and individual states in times of need. Operating under the dual authority of the federal government and the fifty state governors, the Army National Guard provides trained and ready soldiers for overseas military operations, domestic disaster relief, homeland security, and civil support missions. Its primary data and digital services are focused on recruiting, career management, benefits administration, and public outreach. The National Guard Bureau (NGB) coordinates federal operations and maintains administrative systems under Title 10 and Title 32 of the United States Code.
apis:
  - aid: army-national-guard:recruiting-api
    name: Army National Guard Recruiting API
    description: The Army National Guard Recruiting API provides access to job listings, Military Occupational Specialties (MOS), unit locations, and recruiter contact information for prospective members interested in joining the National Guard. This supports the GoArmyGuard.com recruiting portal.
    humanURL: https://www.nationalguard.mil/Portals/31/Documents/About/NGB_Fact_Sheet.pdf
    baseURL: https://www.nationalguard.mil
    tags:
      - Recruiting
      - Military
      - Jobs
      - National Guard
    properties:
      - type: Documentation
        url: https://www.nationalguard.mil/Recruiting/
  - aid: army-national-guard:foia-api
    name: Army National Guard FOIA Portal
    description: The Freedom of Information Act (FOIA) portal for the Army National Guard and National Guard Bureau provides a mechanism for submitting FOIA requests, tracking request status, and accessing previously released records. Managed under the NGB FOIA Policy.
    humanURL: https://www.nationalguard.mil/About/FOIA/
    baseURL: https://www.nationalguard.mil
    tags:
      - FOIA
      - Government
      - Transparency
      - Open Government
    properties:
      - type: Documentation
        url: https://www.nationalguard.mil/About/FOIA/
common:
  - type: Portal
    url: https://www.nationalguard.mil/
    title: Army National Guard Website
  - type: Documentation
    url: https://www.nationalguard.mil/Resources/
    title: Resources
  - type: GitHubOrganization
    url: https://github.com/armyguard
    title: Army Guard GitHub Organization
  - type: TermsOfService
    url: https://www.nationalguard.mil/About/Web-Policy/
    title: Web Policy and Terms
  - type: PrivacyPolicy
    url: https://www.nationalguard.mil/About/Web-Policy/
    title: Privacy Policy
  - type: Features
    data:
      - name: Recruiting Portal
        description: GoArmyGuard.com and the main recruiting portal allow prospective soldiers to search job listings by MOS, state, and skill, and connect with local recruiters.
      - name: FOIA Request System
        description: Online submission and tracking system for Freedom of Information Act requests to the National Guard Bureau and Army National Guard.
      - name: Soldier Self-Service Portal
        description: Current soldiers access pay, benefits, training records, and deployment orders through the Army self-service portal integrated with the National Guard.
      - name: Unit Locator
        description: Public-facing tool allowing citizens to find Army National Guard units and armory locations in their state or territory.
  - type: UseCases
    data:
      - name: Recruit Prospective Soldiers
        description: Recruiters and prospective enlistees use the recruiting portal to search available MOS positions, explore benefits, and initiate the enlistment process.
      - name: Submit FOIA Requests
        description: Journalists, researchers, and citizens submit Freedom of Information Act requests for Army National Guard records and documents.
      - name: Locate National Guard Units
        description: Citizens and emergency managers find local National Guard units and armory locations for community engagement or emergency coordination.
      - name: Access Soldier Benefits Information
        description: Soldiers and their families access information on benefits including education assistance (Montgomery GI Bill), healthcare (TRICARE), and retirement benefits.
  - type: Integrations
    data:
      - name: USA Jobs
        description: Army National Guard job listings integrate with USAJobs.gov, the federal government's official employment site, for civil service and technician positions.
      - name: MyArmyBenefits
        description: Integration with the Army's official benefits counseling portal (myarmybenefits.us.army.mil) for National Guard member benefits information.
      - name: Army Training Requirements and Resources System (ATRRS)
        description: Training management system used by the National Guard to manage soldier training requirements and school seat reservations.
      - name: Defense Finance and Accounting Service (DFAS)
        description: Financial management integration for National Guard pay, travel reimbursement, and benefits payments processed through DFAS.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
