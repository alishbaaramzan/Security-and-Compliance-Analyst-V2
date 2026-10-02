"""evidence list per requirement"""

EVIDENCE_REQUIREMENTS: dict[str, list[dict]] = {
    "AI-001": [
        {
            "evidence_id": "AI-001-E1",
            "question": "Is a specific person or role named as accountable for the application?",
            "applies_when": "always",
            "red_flag": "Only 'the team', 'IT', or no one is mentioned.",
        },
        {
            "evidence_id": "AI-001-E2",
            "question": "Does that owner sit in the business, not only in IT or the vendor?",
            "applies_when": "always",
            "red_flag": "Ownership sits entirely with a technical function or vendor.",
        },
    ],
    "AI-002": [
        {
            "evidence_id": "AI-002-E1",
            "question": "What data is sent to the AI system, and is any of it sensitive (personal, financial, health, confidential, source code)?",
            "applies_when": "always",
            "red_flag": "Data types are not described at all.",
        },
        {
            "evidence_id": "AI-002-E2",
            "question": "If sensitive, what controls apply (masking, redaction, private or approved deployment, no-training contract terms)?",
            "applies_when": "sensitive data is involved",
            "red_flag": "Sensitive data goes to a public tool with no controls.",
        },
        {
            "evidence_id": "AI-002-E3",
            "question": "Is it stated where the data is sent (which provider, region, or environment)?",
            "applies_when": "sensitive data is involved",
            "red_flag": "Destination of sensitive data is unspecified.",
        },
    ],
    "AI-003": [
        {
            "evidence_id": "AI-003-E1",
            "question": "What business decisions or actions does the AI output feed into?",
            "applies_when": "always",
            "red_flag": "Output drives decisions but the decisions are not described.",
        },
        {
            "evidence_id": "AI-003-E2",
            "question": "Does a human review or approve the output before it takes effect?",
            "applies_when": "output is used for business decisions",
            "red_flag": "'Fully automated' or 'auto-approved' with no review step.",
        },
        {
            "evidence_id": "AI-003-E3",
            "question": "Can the reviewer override or reject the output, and are they qualified to judge it?",
            "applies_when": "output is used for business decisions",
            "red_flag": "Review is a rubber stamp, or the reviewer cannot override.",
        },
    ],
    "AI-004": [
        {
            "evidence_id": "AI-004-E1",
            "question": "Is it stated what is logged (prompts, outputs, user actions, errors)?",
            "applies_when": "always",
            "red_flag": "Explicitly no logging, or logging mentioned with no detail.",
        },
        {
            "evidence_id": "AI-004-E2",
            "question": "Does someone or something review the logs or alert on issues (misuse, drift, failures)?",
            "applies_when": "always",
            "red_flag": "Logs are collected but never reviewed.",
        },
        {
            "evidence_id": "AI-004-E3",
            "question": "Is a log retention period or storage location mentioned?",
            "applies_when": "logging exists",
            "red_flag": "Logs are kept indefinitely or stored somewhere uncontrolled.",
        },
    ],
    "AI-005": [
        {
            "evidence_id": "AI-005-E1",
            "question": "Is it defined who is allowed to use the application?",
            "applies_when": "always",
            "red_flag": "Open to everyone, or the user group is undefined.",
        },
        {
            "evidence_id": "AI-005-E2",
            "question": "Is the enforcement mechanism stated (SSO, role-based permissions, MFA)?",
            "applies_when": "always",
            "red_flag": "Shared accounts, shared API keys, or no authentication.",
        },
        {
            "evidence_id": "AI-005-E3",
            "question": "Are different roles given different levels of access (e.g. admin vs. user)?",
            "applies_when": "multiple user types exist",
            "red_flag": "Everyone has the same privileges, including admin functions.",
        },
    ],
    "AI-006": [
        {
            "evidence_id": "AI-006-E1",
            "question": "Are any third-party models or services used, and which ones?",
            "applies_when": "always",
            "red_flag": "A third-party tool is implied but not named.",
        },
        {
            "evidence_id": "AI-006-E2",
            "question": "Is there evidence of a security or vendor assessment (questionnaire, certification review, approval record)?",
            "applies_when": "a third-party model or service is used",
            "red_flag": "Third party is named but nothing about assessment.",
        },
        {
            "evidence_id": "AI-006-E3",
            "question": "Is it stated who performed or approved the assessment and roughly when?",
            "applies_when": "a third-party model or service is used",
            "red_flag": "Claims of assessment with no owner or date.",
        },
    ],
    "AI-007": [
        {
            "evidence_id": "AI-007-E1",
            "question": "Is the intended purpose of the application clearly described?",
            "applies_when": "always",
            "red_flag": "Vague purpose such as 'to improve productivity'.",
        },
        {
            "evidence_id": "AI-007-E2",
            "question": "Are limitations or out-of-scope uses stated (known errors, what it must not be used for)?",
            "applies_when": "always",
            "red_flag": "Purpose is stated but limitations are absent.",
        },
        {
            "evidence_id": "AI-007-E3",
            "question": "Is this documented somewhere users can find it, rather than only mentioned in passing?",
            "applies_when": "always",
            "red_flag": "No indication it is written down or shared with users.",
        },
    ],
    "AI-008": [
        {
            "evidence_id": "AI-008-E1",
            "question": "Does the use case have high-risk characteristics (affects people's rights, finances, health, employment, safety, or legal outcomes)?",
            "applies_when": "always",
            "red_flag": "High-risk characteristics are present but never acknowledged.",
        },
        {
            "evidence_id": "AI-008-E2",
            "question": "If high-risk, has additional review (risk, legal, ethics, security) been completed or scheduled before deployment?",
            "applies_when": "the use case is high-risk",
            "red_flag": "High-risk use case heading to deployment with no extra review.",
        },
        {
            "evidence_id": "AI-008-E3",
            "question": "Is it clear who performs or approves that review?",
            "applies_when": "the use case is high-risk",
            "red_flag": "Review is mentioned but no reviewer or body is named.",
        },
    ],
}