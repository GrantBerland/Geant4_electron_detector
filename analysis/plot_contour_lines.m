%% Loads (x,y,z) positional hits and momentum (x,y,z) components
load('angled_run.mat');

%% Scatter Plot with Contours
figure();
hold on;
scatter(X,Z, 'b.');
[n,c] = hist3([X, Z]);
contour(c{1}, c{2}, n);

%% Creates histogrammed data and surface plot

% 2D histogram counts stored in N
figure();
[N,~,~] = histcounts2(X,Z);
surface(N);


%%  Gaussian 2D Rotational Fit

[N,~,~] = histcounts2(X,Z);
options = ['Robust','on']; 
[fitresult, gof] = gauss2DRotFit(N, options);
