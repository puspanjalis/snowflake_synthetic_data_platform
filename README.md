# Snowflake Synthetic Data Platform

[![Python](https://img.shields.io/badge/Python-63.2%25-blue)](#)
[![PLpgSQL](https://img.shields.io/badge/PLpgSQL-36.8%25-green)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An enterprise-grade synthetic data generation framework for Snowflake that enables secure, compliant data generation for testing and development environments.

## 🎯 Overview

This platform provides a comprehensive solution for generating realistic synthetic data within Snowflake, combining native Snowflake capabilities with robust fallback mechanisms and enterprise-grade validation.

## ✨ Features

- **Native Synthetic Generation**: Leverages Snowflake's `GENERATE_SYNTHETIC_DATA()` function
- **Empirical Fallback Generation**: Automatic fallback mechanism for enhanced data generation
- **Referential Integrity Validation**: Ensures data consistency and relationship integrity
- **Statistical Realism**: Maintains statistical properties of original datasets
- **Streamlit UI**: User-friendly web interface for data generation workflows
- **Batch Processing**: Efficient large-scale data generation with batch-safe execution
- **Production Observability**: Comprehensive audit logging and monitoring
- **Snowpark Integration**: Native Python/Scala integration with Snowpark

## 🏗️ Project Structure

```
snowflake_synthetic_data_platform/
├── README.md                                        # This file
├── LICENSE                                          # MIT License
├── streamlit_app.py                                # Streamlit web application
├── generate_and_validate_synthetic_data_audit.sql  # Audit procedures
├── sp_fake_synthetic_data.sql                      # Main generation procedures
├── docs/                                            # Documentation
├── examples/                                        # Usage examples
├── snowflake/                                       # Snowflake-specific code
└── stored_procedures/                               # SQL stored procedures
```

## 🚀 Quick Start

### Prerequisites

- Snowflake account with appropriate permissions
- Python 3.8 or higher
- Streamlit
- Required Python dependencies

### Installation

1. Clone the repository:
```bash
git clone https://github.com/puspanjalis/snowflake_synthetic_data_platform.git
cd snowflake_synthetic_data_platform
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your Snowflake connection:
```bash
# Set your Snowflake credentials
export SNOWFLAKE_ACCOUNT=<your_account>
export SNOWFLAKE_USER=<your_user>
export SNOWFLAKE_PASSWORD=<your_password>
export SNOWFLAKE_WAREHOUSE=<your_warehouse>
```

### Deployment

1. **Deploy SQL Procedures** (to your Snowflake environment):
   - Run `sp_fake_synthetic_data.sql` to create main generation procedures
   - Run `generate_and_validate_synthetic_data_audit.sql` for audit functionality

2. **Launch Streamlit App**:
```bash
streamlit run streamlit_app.py
```

3. Access the application at `http://localhost:8501`

## 📖 Usage

### Via Streamlit UI

1. Open the application in your browser
2. Select your target table
3. Specify the number of synthetic records needed
4. Configure generation parameters
5. Review generated data and validation results

### Via SQL

```sql
-- Generate synthetic data using stored procedures
CALL sp_fake_synthetic_data(
    p_table_name => 'YOUR_TABLE',
    p_record_count => 1000
);

-- Validate generated data
CALL generate_and_validate_synthetic_data_audit();
```

## 🔧 Configuration

### Snowflake Settings

Configure the following in your Snowflake environment:
- Database and schema for synthetic data
- Warehouse size for generation jobs
- Retention policies for synthetic data

### Application Settings

See `docs/` for detailed configuration documentation.

## 📚 Documentation

Comprehensive documentation is available in the `docs/` directory:
- Architecture overview
- API reference
- Configuration guide
- Best practices

## 💡 Examples

Example workflows and use cases are available in the `examples/` directory.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Support

For issues, questions, or suggestions, please open a [GitHub Issue](https://github.com/puspanjalis/snowflake_synthetic_data_platform/issues).

## 🙏 Acknowledgments

- Snowflake for the synthetic data generation capabilities
- Streamlit for the excellent UI framework
- The open-source community

---

**Last Updated**: 2026-05-14

