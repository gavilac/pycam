#!/usr/bin/env python

"""

Notes and code for plotting and testing the apps

Brian
"""
import pylab


def plot_compare(data, title, show=False):
    python_cv_title = 'OPENCV_PY'
    c_title = 'OPENCV_C'
    scipy_title = 'SCIPY'
    try:
        python_data, c_data, scipy_data = data
        SCIPY = True
        
    except:
        python_data, c_data = data
        SCIPY = False
    
    x = 1+pylab.arange(len(data))  # Either 2 or 3...

    pylab.title(title)
    
    all_data = pylab.array(data).flatten()
    
    bars = pylab.bar( (1), ( python_data.mean() ), yerr=python_data.std(), width=0.8, color='#88aa33', align='center', ecolor='black', capsize=50)
    bars2 = pylab.bar((2), ( c_data.mean()      ), yerr=c_data.std(),      width=0.8, color='#774499', align='center', ecolor='black', capsize=50)
    
    #pylab.errorbar(x, 
    #    [d.mean() for d in data], 
    #    [d.std() for d in data],
    #    fmt=None,
    #     marker='', mec='green', ms=300, mew=5)
    
    if SCIPY: 
        bars3 = pylab.bar((3), scipy_data.mean(), yerr=scipy_data.std(), width=0.8, color='red', align='center', ecolor='black', capsize=50)
        #pylab.legend((bars[0], bars2[0], bars3[0]), (python_cv_title,c_title ))
        pylab.xticks((1,2,3),(python_cv_title, c_title, scipy_title))
    else:
        pylab.xticks((1,2),(python_cv_title, c_title))
        #pylab.legend((bars[0], bars2[0]), (python_cv_title,c_title ))
    
    pylab.xlabel('Programming Language')
    
    pylab.ylabel('Frames Per Second')
    ymin = all_data.min() - 2*all_data.std()
    if ymin < 0:ymin=0
    yaxis = pylab.linspace(ymin,all_data.max() + 1*all_data.std(),10)
    
    pylab.ylim(ymin, all_data.max() + 2*all_data.std())
    pylab.yticks(yaxis,["%.3f" % i for i in yaxis])
    pylab.savefig("%s.png" % "_".join(title.lower().split(" ")), transparent=True)

    if show:
        pylab.show()

def plot_webcam_results():
    """I also did pygame here - it was also bang on 15 fps"""
    py_webcam_stream = pylab.array([15.0073, 15.0033,	15.0072]) #, 15.005808])
    cpp_webcam_stream = pylab.array([15.0170, 15.0092,	15.0101])#, 15.0177])
    plot_compare((py_webcam_stream, cpp_webcam_stream),"Streaming from webcam in OpenCV", True)


def plot_gaussian_results():
    py_gaussian = pylab.array([ 14.555189, 14.736740, 14.974582, 14.7518])
    scipy_gaussian = pylab.array([8.026670, 7.9043, 7.7535,  8.0019])   
    cpp_gaussian = pylab.array([14.7219, 14.6268, 14.6117, 15.246])    # mean: 14.6534, std: 0.048780
    plot_compare(pylab.array([py_gaussian, cpp_gaussian, scipy_gaussian ]),"Gaussian Blur", True)

def plot_background():
    cpp_cv = pylab.array([7.8598, 7.9791, 7.93613, 7.906, 7.766    ])    # mean: 14.6534, std: 0.048780
    py_cv = pylab.array([7.61715, 8.044 , 7.8716 , 8.046, 8.047115 ])
    scipy_one = pylab.array([7.581724, 7.815616, 7.481059, 7.52825, 7.014058])
    plot_compare(pylab.array([py_cv, cpp_cv, scipy_one]),"Background Subtraction", True)

if __name__ == "__main__":
    print "Plotting results now"
    pylab.figure()
    plot_webcam_results()
    pylab.figure()
    plot_gaussian_results() 
    pylab.figure()
    plot_background()



#py_ = pylab.array([ ])
#scipy_ = pylab.array([])
#cpp_ = pylab.array([])

#plot_compare(pylab.array([py_, cpp_, scipy_ ]),"title", True)

