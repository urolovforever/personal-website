import React from 'react';
import { FaGraduationCap, FaBriefcase, FaCertificate } from 'react-icons/fa';

const Resume = () => {
  const education = [
    {
      degree: 'Bachelor of Science in Computer Science',
      institution: 'University Name',
      period: '2018 - 2022',
      description: 'Focus on software engineering, algorithms, and data structures.',
    },
  ];

  const experience = [
    {
      position: 'Senior Full Stack Developer',
      company: 'Tech Company Inc.',
      period: '2022 - Present',
      description: 'Leading development of scalable web applications using React and Django.',
      achievements: [
        'Improved application performance by 40%',
        'Mentored junior developers',
        'Implemented CI/CD pipeline',
      ],
    },
    {
      position: 'Full Stack Developer',
      company: 'Startup XYZ',
      period: '2020 - 2022',
      description: 'Developed and maintained multiple client projects.',
      achievements: [
        'Built 5+ production applications',
        'Reduced bugs by 30% through testing',
        'Collaborated with cross-functional teams',
      ],
    },
  ];

  const skills = {
    'Frontend': ['React', 'JavaScript/TypeScript', 'HTML/CSS', 'Tailwind CSS', 'Redux'],
    'Backend': ['Django', 'Node.js', 'Python', 'REST APIs', 'PostgreSQL'],
    'Tools & Others': ['Git', 'Docker', 'AWS', 'CI/CD', 'Agile/Scrum'],
  };

  const certifications = [
    {
      name: 'AWS Certified Developer',
      issuer: 'Amazon Web Services',
      year: '2023',
    },
    {
      name: 'Professional Scrum Master',
      issuer: 'Scrum.org',
      year: '2022',
    },
  ];

  return (
    <section id="resume" className="py-20 px-4 sm:px-6 lg:px-8 bg-gray-50 dark:bg-gray-800">
      <div className="max-w-7xl mx-auto">
        <h2 className="section-title">Resume</h2>

        {/* Skills Section */}
        <div className="mb-16">
          <h3 className="text-3xl font-bold text-gray-900 dark:text-white mb-8 flex items-center">
            <span className="w-2 h-8 bg-primary-600 rounded-full mr-4"></span>
            Skills
          </h3>
          <div className="grid md:grid-cols-3 gap-6">
            {Object.entries(skills).map(([category, skillList]) => (
              <div key={category} className="card p-6">
                <h4 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
                  {category}
                </h4>
                <div className="flex flex-wrap gap-2">
                  {skillList.map((skill) => (
                    <span
                      key={skill}
                      className="px-3 py-1 bg-primary-100 dark:bg-primary-900 text-primary-700 dark:text-primary-300 rounded-full text-sm font-medium"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Experience Section */}
        <div className="mb-16">
          <h3 className="text-3xl font-bold text-gray-900 dark:text-white mb-8 flex items-center">
            <FaBriefcase className="text-primary-600 mr-4" />
            Experience
          </h3>
          <div className="space-y-6">
            {experience.map((exp, index) => (
              <div key={index} className="card p-6">
                <div className="flex flex-col md:flex-row md:justify-between md:items-start mb-4">
                  <div>
                    <h4 className="text-xl font-semibold text-gray-900 dark:text-white">
                      {exp.position}
                    </h4>
                    <p className="text-primary-600 dark:text-primary-400 font-medium">
                      {exp.company}
                    </p>
                  </div>
                  <span className="text-gray-600 dark:text-gray-400 text-sm md:text-base mt-2 md:mt-0">
                    {exp.period}
                  </span>
                </div>
                <p className="text-gray-700 dark:text-gray-300 mb-4">
                  {exp.description}
                </p>
                <ul className="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-400">
                  {exp.achievements.map((achievement, i) => (
                    <li key={i}>{achievement}</li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>

        {/* Education Section */}
        <div className="mb-16">
          <h3 className="text-3xl font-bold text-gray-900 dark:text-white mb-8 flex items-center">
            <FaGraduationCap className="text-primary-600 mr-4" />
            Education
          </h3>
          <div className="space-y-6">
            {education.map((edu, index) => (
              <div key={index} className="card p-6">
                <div className="flex flex-col md:flex-row md:justify-between md:items-start mb-4">
                  <div>
                    <h4 className="text-xl font-semibold text-gray-900 dark:text-white">
                      {edu.degree}
                    </h4>
                    <p className="text-primary-600 dark:text-primary-400 font-medium">
                      {edu.institution}
                    </p>
                  </div>
                  <span className="text-gray-600 dark:text-gray-400 text-sm md:text-base mt-2 md:mt-0">
                    {edu.period}
                  </span>
                </div>
                <p className="text-gray-700 dark:text-gray-300">
                  {edu.description}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Certifications Section */}
        <div>
          <h3 className="text-3xl font-bold text-gray-900 dark:text-white mb-8 flex items-center">
            <FaCertificate className="text-primary-600 mr-4" />
            Certifications
          </h3>
          <div className="grid md:grid-cols-2 gap-6">
            {certifications.map((cert, index) => (
              <div key={index} className="card p-6">
                <h4 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                  {cert.name}
                </h4>
                <p className="text-primary-600 dark:text-primary-400 font-medium mb-1">
                  {cert.issuer}
                </p>
                <p className="text-gray-600 dark:text-gray-400 text-sm">
                  {cert.year}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Resume;
