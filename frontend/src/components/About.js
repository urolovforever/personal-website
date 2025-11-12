import React from 'react';
import { FaCode, FaLightbulb, FaRocket } from 'react-icons/fa';

const About = () => {
  const highlights = [
    {
      icon: FaCode,
      title: 'Clean Code',
      description: 'Writing maintainable and efficient code following best practices',
    },
    {
      icon: FaLightbulb,
      title: 'Problem Solver',
      description: 'Finding creative solutions to complex technical challenges',
    },
    {
      icon: FaRocket,
      title: 'Fast Learner',
      description: 'Quickly adapting to new technologies and frameworks',
    },
  ];

  return (
    <section id="about" className="py-20 px-4 sm:px-6 lg:px-8 bg-white dark:bg-gray-900">
      <div className="max-w-7xl mx-auto">
        <h2 className="section-title">About Me</h2>

        <div className="grid md:grid-cols-2 gap-12 items-center">
          {/* Left side - Text content */}
          <div className="space-y-6">
            <p className="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
              Hello! I'm a passionate <span className="font-semibold text-primary-600 dark:text-primary-400">Full Stack Developer</span> with
              experience in building web applications from concept to deployment. I love turning
              complex problems into simple, beautiful, and intuitive solutions.
            </p>

            <p className="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
              I specialize in <span className="font-semibold text-primary-600 dark:text-primary-400">modern web technologies</span> including
              React, Django, Node.js, and more. I'm always eager to learn new technologies and
              stay up-to-date with the latest industry trends.
            </p>

            <p className="text-lg text-gray-700 dark:text-gray-300 leading-relaxed">
              When I'm not coding, you can find me exploring new technologies, contributing to
              open-source projects, or sharing knowledge with the developer community.
            </p>

            <div className="pt-4">
              <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
                Fun Fact
              </h3>
              <p className="text-lg text-gray-700 dark:text-gray-300 italic">
                I believe the best code is the code you don't have to write. Simplicity is the
                ultimate sophistication.
              </p>
            </div>
          </div>

          {/* Right side - Highlights */}
          <div className="space-y-6">
            {highlights.map((highlight, index) => (
              <div
                key={index}
                className="card p-6 flex items-start space-x-4"
              >
                <div className="flex-shrink-0">
                  <div className="w-12 h-12 rounded-lg bg-primary-100 dark:bg-primary-900 flex items-center justify-center">
                    <highlight.icon className="w-6 h-6 text-primary-600 dark:text-primary-400" />
                  </div>
                </div>
                <div>
                  <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                    {highlight.title}
                  </h3>
                  <p className="text-gray-600 dark:text-gray-400">
                    {highlight.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
