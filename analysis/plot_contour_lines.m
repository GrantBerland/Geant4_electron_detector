
figure();
hold on;
scatter(X,Z, 'b.');
[n,c] = hist3([X, Z]);
contour(c{1}, c{2}, n);

% 2D histogram counts stored in N
[N,~,~] = histcounts2(X,Y);