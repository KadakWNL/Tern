// PDFReport.jsx
import React from 'react';
import { Document, Page, View, Text, Image, StyleSheet } from '@react-pdf/renderer';

// Define styles for the PDF
const styles = StyleSheet.create({
  page: {
    flexDirection: 'column',
    backgroundColor: '#ffffff',
    padding: 20,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#1e3a8a',
    color: '#ffffff',
    padding: 20,
  },
  logo: {
    width: 80,
    height: 80,
    marginRight: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  section: {
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  label: {
    fontSize: 14,
    fontWeight: 'bold',
  },
  value: {
    fontSize: 14,
  },
  chartPlaceholder: {
    width: '100%',
    height: 200,
    backgroundColor: '#f3f4f6',
    justifyContent: 'center',
    alignItems: 'center',
  },
  footer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#f3f4f6',
  },
});

const PDFReport = ({ studentInfo, studentSPI, classSPI }) => {
  return (
    <Document>
      <Page size="A4" style={styles.page}>
        {/* Header */}
        <View style={styles.header}>
          <Image src="/path/to/logo.png" style={styles.logo} />
          <Text style={styles.title}>Manyu Classes</Text>
        </View>

        {/* Report Card Title */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>REPORT CARD</Text>
          <View style={{ borderTop: '2px solid #1e3a8a', marginHorizontal: 50 }} />
        </View>

        {/* Student Information */}
        <View style={styles.section}>
          <View style={styles.row}>
            <View>
              <Text style={styles.label}>Student Name:</Text>
              <Text style={styles.value}>{studentInfo.name}</Text>
            </View>
            <View>
              <Text style={styles.label}>Student No.:</Text>
              <Text style={styles.value}>{studentInfo.studentNo}</Text>
            </View>
          </View>
          <View style={styles.row}>
            <View>
              <Text style={styles.label}>Course:</Text>
              <Text style={styles.value}>{studentInfo.course}</Text>
            </View>
            <View>
              <Text style={styles.label}>Major:</Text>
              <Text style={styles.value}>{studentInfo.major}</Text>
            </View>
          </View>
        </View>

        {/* Charts Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Performance Charts</Text>
          <View style={styles.chartPlaceholder}>
            <Text>Charts will be rendered here</Text>
          </View>
        </View>

        {/* Footer */}
        <View style={styles.footer}>
          <Text>Made with ❤️ by Tern</Text>
          <Image src="/path/to/tern-logo.png" style={{ width: 60, height: 30 }} />
        </View>
      </Page>
    </Document>
  );
};

export default PDFReport;