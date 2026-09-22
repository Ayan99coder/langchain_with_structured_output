review_schema = {
    "title": "ProductReview",
    "description": "Extract structured information from a product review.",

    "type": "object",

    "properties": {
        "product_name": {
            "type": "string",
            "description": "Name of the product being reviewed."
        },

        "reviewer_name": {
            "type": "string",
            "description": "Name of the person who wrote the review."
        },

        "reviewer_email": {
            "type": "string",
            "format": "email",
            "description": "Email address of the reviewer, if provided."
        },

        "review_text": {
            "type": "string",
            "description": "The complete original product review."
        },

        "rating": {
            "type": "integer",
            "minimum": 1,
            "maximum": 5,
            "description": "Rating out of 5, only if explicitly provided."
        },

        "pros": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Positive features mentioned in the review."
        },

        "cons": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Negative features or limitations mentioned in the review."
        },

        "summary": {
            "type": "string",
            "description": "A short summary of the review."
        },

        "recommendation": {
            "type": "string",
            "enum": [
                "recommended",
                "not_recommended",
                "conditional",
                "not_specified"
            ],
            "description": "Recommendation based on the review."
        },

        "battery_condition_mentioned": {
            "type": "boolean",
            "description": "Whether battery health or condition is discussed."
        }
    },

    "required": [
        "product_name",
        "reviewer_name",
        "review_text"
    ],

    "additionalProperties": False
}