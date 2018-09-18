# Overall (77/100)
 - Your commit history doesn't have anything in it: this will work for 
   submission, but obviates the purpose of version control. Commits should be
   made at increments where logical chunks of code, analysis, or text 
   processing is done.

# Build (7/10)
 - Adequate description of process for building report
 - Might want to include information about your environment (python version,
   package dependencies, etc.) to improve portability.
 - Note that your build fails because of absolute-paths specified in 
   `code/spectrum_cal.py`. This is a common issue - a good way to catch it in
   the future is to clone onto a clean system and try to build everything
   before submitting.

# Testing (10/10)
 - Originally failed because of build issue above, but adequately designed
   test

# Intro / Background / Motivation (13/15)
 - Content is adequate for lab 0, but looks like it may have been a rough
   draft - missing citations

# Methods (10/15)
 - Though the task for lab 0 was intentionally trivial, it is important to 
   recognize which components of analysis should be expanded on. For example, 
   energy calibration requires subtasks of both peak-finding and peak-fitting.
   A discussion of your approach to implementing these components would be 
   warranted here.
 - Note the parameters determined for your calibration model probably belong
   in the results section

# Results and discussion (30/40)
 - Significant figures are important - the presented values imply a level of
   precision far greater than what is actually achieved.
 - As mentioned in the methods, inadequate consideration is given to the 
   components of energy calibration, so it is not possible to conduct a 
   meaningful uncertainty analysis.
 - Plots are well-labeled and captions of the appropriate level of detail, but
   don't convey much information. For instance, rather than show figure 2 as is,
   consider plotting the residual of the energy calibration fit vs. energy

# Conclusion (7/10)
 - A separate conclusion section is not required - the discussion can serve for
   our purposes.
 - You're on the right track in terms of identifying the limitations of the
   given methodology, but the statements are not well-supported by the data.
   Using more than two lines will allow for a characterization of the linearity
   of the energy calibration model, but would not necessarily be expected to
   improve things (by using a two point calibration, we are essential assuming
   deviations from linearity are less than the level of precison we care about).
   However, using more precise data and addressing the limitations in the
   peak-fitting would be expected to improve the precision and accuracy of the
   model, respectively.
